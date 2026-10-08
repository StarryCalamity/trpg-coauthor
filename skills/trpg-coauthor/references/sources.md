# 来源、改编与许可

本包是独立的中文TRPG共同创作技能。它整合已有AI技能的适用方法及公开TRPG设计思路，并重新编写工作流、模板、例子与检查。来源记录用于追溯，不是运行依赖；本包无需安装下列技能或联网加载文章。

## 外部AI技能

### gm-apprentice / ttrpg-expert

- 作者／维护者：AntTheLimey及gm-apprentice贡献者。
- 仓库：[AntTheLimey/gm-apprentice](https://github.com/AntTheLimey/gm-apprentice)。
- 参考版本：`a0215b1f2e688c476e37d372fd647935360f00b8`。
- 参考文件：`skills/ttrpg-expert/scene-encounter-patterns.md`、`scenario-writing.md`，以及其NPC、连续性与主持材料。
- 改编：情境设计、主持人信息与玩家信息分离、NPC反应依据、不同场景的运行准备与连续性检查。中文版重新组织，删除固定人数、轮数与句数要求，删除vault流程及其他技能依赖，并对日常、线性模组和失败后果作适用条件说明。
- 上游原始Markdown与技能材料采用[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)，本包的整合改编材料沿用该许可，完整文本见根目录`LICENSE`。
- 未包含上游游戏规则摘录、系统数据、Python代码或第三方规则授权内容；其MIT代码及SRD等授权不作为本包规则资料的来源。

### novel-writing

- 作者／维护者：wgwtest。
- 仓库：[wgwtest/novel-writing](https://github.com/wgwtest/novel-writing)。
- 参考版本：`838729695148008d42c01bd7c3c0c1a5c15de830`。
- 参考文件：`novel-writing/SKILL.md`及对白行为、人物认知、场景因果、文风与修订材料。
- 改编：区分知识层次、关注对白对当前互动的作用、按原文保留人物声音、局部修复而非文风统一。将小说中的完整人物行动链改为主持人的NPC反应依据，不将作者对角色行动的控制移交到玩家角色。
- 上游采用MIT许可，版权与完整许可保留于根目录`LICENSE.novel-writing`。本包没有打包原小说项目管理系统与脚本。

## TRPG方法的一手来源

以下内容为方法归纳与适用性判断，未转载文章正文。作者名与标题保留用于查证；引用不表示原作者为本包背书。

- Justin Alexander：[Don't Prep Plots](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots)。准备局势、动机与可作用的内容，避免依赖玩家唯一的预期反应。本包保留线性结构及约定开场的使用空间。
- Justin Alexander：[Game Structure: Party Planning](https://thealexandrian.net/wordpress/37995/roleplaying-games/game-structure-party-planning)。空间、人物、事件与话题支持群体社交；本包按场景规模调整，不沿用固定人数与事件数量。
- Justin Alexander：[Universal NPC Roleplaying Template](https://thealexandrian.net/wordpress/37916/roleplaying-games/universal-npc-roleplaying-template)。让外观、扮演依据、背景与关键资料易于检索；本包补充当前目标、知识、权限与边界。
- Justin Alexander：[Three Clue Rule](https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule)。关键结论的冗余证据；本包强调独立获得渠道与系统差异。
- Mike Shea / Sly Flourish：[Lazy GM Resource Document](https://slyflourish.com/lazy_gm_resource_document.html)。根据角色、潜在场景、信息、地点和NPC准备可即兴使用的素材；不把完整备团清单强加到每次局部修改。
- Mike Shea / Sly Flourish：[The Near Perfect RPG Session](https://slyflourish.com/near_perfect_dnd_game.html)。以可响应玩家行动的准备支持游玩。其经验不能证明本技能必然改善玩家情感投入。
- Chaosium：[Roleplaying Game Submissions](https://www.chaosium.com/roleplaying-game-submissions/)。玩家参与中心与有用的背景信息；出版社的题材、格式及投稿要求不视作所有TRPG的规范。

## 技能结构规范

- OpenAI：[Build skills](https://developers.openai.com/plugins/build/skills)。入口元数据、明确边界、按需读取参考与模板；不为纯创作工作增加没有必要的执行脚本。
- OpenAI：[Skills](https://developers.openai.com/api/docs/guides/tools-skills)。技能目录与单一顶层目录的ZIP包结构。
- `agents/openai.yaml`遵循Codex内置skill-creator的界面字段规范。本包不声明MCP依赖或固定模型。

这些技能与文章是来源资料，安装、格式检查或设计推演均不等于实际带团验证。本包不包含用户原稿、项目专属设定或个人信息。技能文本的许可不改变使用者原稿或创作产物的权利。
