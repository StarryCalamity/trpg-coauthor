"""Check portable skill content and optionally build distribution archives."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'trpg-coauthor'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def check() -> dict:
    text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
    require(match is not None, 'Missing YAML frontmatter')
    metadata = yaml.safe_load(match.group(1))
    require(isinstance(metadata, dict), 'Frontmatter must be a mapping')
    require(metadata.get('name') == SKILL.name, 'Skill name must match its directory')
    require(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', metadata['name'])), 'Invalid skill name')
    require(len(metadata['name']) <= 64, 'Skill name too long')
    description = metadata.get('description')
    require(isinstance(description, str) and 0 < len(description) <= 1024, 'Invalid description')
    require('<' not in description and '>' not in description, 'Angle brackets in description')
    require(not (set(metadata) - {'name', 'description', 'license', 'allowed-tools', 'metadata'}), 'Unexpected frontmatter fields')

    ui_config = yaml.safe_load((SKILL / 'agents/openai.yaml').read_text(encoding='utf-8'))
    ui = ui_config['interface']
    require(25 <= len(ui['short_description']) <= 64, 'Invalid UI description length')
    require('$trpg-coauthor' in ui['default_prompt'], 'Default prompt must invoke this skill')
    require(not ui_config.get('dependencies'), 'This instruction-only skill must remain independent')

    manifest = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
    require(manifest.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Wrong portable plugin schema')
    require(manifest.get('name') == SKILL.name, 'Plugin identity mismatch')
    require(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', ''))), 'Invalid package version')
    require(not ({'mcpServers', 'apps', 'hooks', 'skills'} & set(manifest)), 'Portable paths are discovered from fixed directories')
    require((ROOT / 'LICENSE').read_bytes() == (SKILL / 'LICENSE').read_bytes(), 'License copies differ')
    require((SKILL / 'LICENSE.novel-writing').is_file(), 'Missing upstream MIT notice')

    files = sorted(p for p in SKILL.rglob('*') if p.is_file())
    require(bool(files), 'Empty package')
    for p in SKILL.rglob('*'):
        require(not p.is_symlink(), f'Symlink in skill: {p.relative_to(SKILL)}')
    links = 0
    for p in files:
        if p.suffix not in {'.md', '.yaml'}:
            continue
        body = p.read_text(encoding='utf-8')
        require(not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]|\$\{CLAUDE_PLUGIN_ROOT\}|\[TODO:', body), f'Nonportable path or unfinished placeholder: {p.relative_to(SKILL)}')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if link.startswith(('https://', 'http://', '#')):
                continue
            target = (p.parent / link.split('#', 1)[0]).resolve()
            require(target.is_relative_to(SKILL), f'Link escapes skill: {link}')
            require(target.is_file(), f'Broken local link: {link}')
            links += 1
    for p in [ROOT / 'README.md', ROOT / 'docs/design-review.md']:
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if link.startswith(('https://', 'http://', '#')):
                continue
            target = (p.parent / link.split('#', 1)[0]).resolve()
            require(target.is_relative_to(ROOT) and target.is_file(), f'Broken repository link: {link}')

    return {'name': metadata['name'], 'version': manifest['version'], 'skill_files': len(files), 'local_skill_links': links}


def write_archive(path: Path, entries: list[tuple[Path, str]]) -> None:
    with ZipFile(path, 'w', ZIP_DEFLATED) as archive:
        for source, name in entries:
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with ZipFile(path) as archive, tempfile.TemporaryDirectory() as temp:
        require(archive.testzip() is None, 'Archive CRC failure')
        for member in archive.namelist():
            parsed = PurePosixPath(member)
            require(not parsed.is_absolute() and '..' not in parsed.parts, 'Unsafe archive path')
            require(parsed.parts[0] == SKILL.name, 'Multiple archive roots')
        archive.extractall(temp)
        for source, name in entries:
            require((Path(temp) / name).read_bytes() == source.read_bytes(), f'Extraction mismatch: {name}')


def build() -> list[Path]:
    destination = ROOT / 'dist'
    destination.mkdir(exist_ok=True)
    skill_files = sorted(p for p in SKILL.rglob('*') if p.is_file())
    skill_zip = destination / 'trpg-coauthor.zip'
    write_archive(skill_zip, [(p, f'trpg-coauthor/{p.relative_to(SKILL).as_posix()}') for p in skill_files])
    package_files = skill_files + [ROOT / 'plugin.json', ROOT / 'README.md', ROOT / 'LICENSE', ROOT / 'docs/design-review.md']
    plugin_zip = destination / 'trpg-coauthor-plugin.zip'
    write_archive(plugin_zip, [(p, f'trpg-coauthor/{p.relative_to(ROOT).as_posix()}') for p in sorted(package_files)])
    sums = ''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in [skill_zip, plugin_zip])
    (destination / 'SHA256SUMS.txt').write_text(sums, encoding='utf-8')
    return [skill_zip, plugin_zip]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true', help='Build and verify release archives')
    args = parser.parse_args()
    result = check()
    if args.build:
        result['archives'] = [p.name for p in build()]
        result['zip_extraction'] = 'passed'
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
