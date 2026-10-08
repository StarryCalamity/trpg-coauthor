# TRPG模组共创 · trpg-coauthor

面向作者与主持人的中文TRPG共同创作技能：把构想和已有原稿整理成能在桌上运行的模组内容，并保留人物声音、潜台词与文学表达。

适用范围包括情境与时间线、调查线索、日常社交与关系发展、NPC对白、探索与遭遇、朗读段、主持人说明和玩家资料。跨规则系统，不内置某套游戏的规则库，也不默认自动主持游戏。

## 安装

在Codex中请求内置安装器安装本仓库的技能目录：

```text
使用 $skill-installer 安装 https://github.com/StarryCalamity/trpg-coauthor/tree/main/skills/trpg-coauthor
```

若仓库为私有，安装者需要相应GitHub访问权限。也可以下载Release中的`trpg-coauthor.zip`，将完整的`trpg-coauthor`文件夹放入自己的用户技能目录，或目标项目的`.agents/skills/`目录。不要只复制`SKILL.md`，其参考资料和模板也要保留。

Codex的当前用户技能位置与发现方式见[官方技能文档](https://learn.chatgpt.com/docs/build-skills)。有自定义技能目录的宿主，请使用其配置位置。安装后如果列表未更新，可重启宿主。

本仓库还提供带根目录`plugin.json`的可移植Agent Plugins包；Release中的`trpg-coauthor-plugin.zip`保留该结构。它没有MCP服务、账户连接或运行时依赖。GitHub交付与插件目录审核是不同流程，本仓库不宣称已获官方目录认证。

## 使用

```text
使用 $trpg-coauthor，阅读下面的原稿，修改旅馆中的这一段日常。
保留后续出发日期和人物的既定职责，给玩家实际参与空间。
```

```text
使用 $trpg-coauthor，检查这段调查是否会被一次失败封死。
先指出具体断点，再给出限定范围内的修订。
```

提供当前目标、原稿和已经决定的设定即可；不必先填完全部世界观。精确数值和规则裁定还需要对应系统、版本及房规。输出语言可按用户要求调整。

## 审查入口

- [技能入口](skills/trpg-coauthor/SKILL.md)：定位、触发范围、工作流程与完成标准。
- [日常与社交](skills/trpg-coauthor/references/social-and-downtime.md)：日常参与和关系发展。
- [NPC与对白](skills/trpg-coauthor/references/npc-and-dialogue.md)：人物声音、知识与潜台词。
- [运行审查](skills/trpg-coauthor/references/playability-review.md)：失败、拒绝参与和意外行动。
- [设计推演记录](docs/design-review.md)：具体案例与验证限度。
- [来源与许可](skills/trpg-coauthor/references/sources.md)：上游技能、TRPG方法和改编说明。

技能包内部资料完整，所有本地引用均在包内。未包含个人模组原稿、项目专属设定、凭据或机器路径。社区创作方法不等于经验证的模型效果；初版完成过人工设计推演，尚未经过跨模型盲测或实际带团验证。

## 维护与打包

需要Python 3.11或以上。以下工具只供仓库维护，不是技能使用依赖：

```text
python -m pip install -r requirements-dev.txt
python scripts/check_package.py --build
```

检查技能元数据、界面字段、相对引用、可移植性和许可，生成技能ZIP、可移植插件ZIP与SHA-256校验文件。GitHub Actions在提交和PR上执行相同检查。验证产物在`dist/`，该目录不提交到源码历史。

## 许可

整合后的技能与文档采用[CC BY-SA 4.0](LICENSE)。MIT来源的版权和许可声明保留在[LICENSE.novel-writing](skills/trpg-coauthor/LICENSE.novel-writing)。署名及具体改编范围见来源说明。技能的许可不改变使用者原稿或创作产物的权利。
