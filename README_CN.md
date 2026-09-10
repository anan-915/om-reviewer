# OM Reviewer

[English](README.md)

`om-reviewer` 是一个用于学术论文审稿的 Codex skill，面向运营管理、经济管理、人工智能、区块链、物流、供应链、ESG、CSR 及相关交叉领域。该 skill 以 SCI 一区论文的严谨程度进行评估，同时要求作者意见简洁、直接并以稿件证据为依据。

## 主要功能

- 审查实证研究、理论模型、优化、博弈论、马尔科夫过程、数值模拟、机器学习研究、案例研究、混合方法研究及综述文章。
- 评估研究动机、理论贡献、方法适用性、证据、结论、实践意义、可重复性、诚信风险信号、参考文献、图表和语言。
- 检查核心技术、构念或方案是否与特定行动者、决策、机制、运营问题和结果建立了明确联系。
- 检查数值模拟参数是否获得文献、数据、制度事实或实际案例支持。
- 评估 Management Insights 或同类章节是否提出现实、具体且受证据约束的实践建议。
- 支持初审和返修稿审查。
- 输出中文简要研判、英文保密编辑意见、英文作者意见及作者可见的英文 DOCX。
- 检查审稿结论一致性、标点规则、意见顺序、重复意见和虚构审稿人身份。

## 输出内容

标准工作流依次返回四项内容。

1. 中文简要研判，包括建议结论和决定性理由。
2. 英文保密编辑意见。
3. 可直接提交给作者的英文审稿意见。
4. 仅包含作者可见意见的英文 DOCX 文件。

Skill提供的是审稿建议，而不是编辑部的最终决定。

## 仓库结构

```text
om-reviewer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── review-report-template.docx
├── references/
└── scripts/
    ├── build_review_docx.py
    └── validate_review_output.py
```

`SKILL.md` 保存核心工作流，并仅在相关时读取详细参考文件。两个脚本分别用于确定性验证和DOCX生成。安装和更新时必须保留完整目录，因为该 skill 依赖参考文件、脚本、界面元数据和模板。

## 环境要求

- ChatGPT桌面应用中的Codex、Codex CLI或Codex IDE扩展
- 用于完整读取稿件的PDF和Documents能力
- 使用验证及DOCX脚本时，需要Python 3.10或更高版本
- DOCX生成需要`python-docx`

如果Codex运行环境没有提供依赖，请执行：

```powershell
python -m pip install -r requirements.txt
```

进行本地发布验证时，`requirements-dev.txt`还会安装Skill Creator验证器所需的`PyYAML`。

## 选择安装范围

只选择一种安装范围。不要在多个可发现位置重复安装同名的`om-reviewer`，否则Codex可能显示多个具有相同frontmatter名称的skill。

### 个人安装

如果希望在不同项目中使用该skill，请选择个人安装。内置`$skill-installer`会安装到`$CODEX_HOME/skills/om-reviewer`。未设置`CODEX_HOME`时，默认位置为`~/.codex/skills/om-reviewer`。

OpenAI官方文档还将`$HOME/.agents/skills/om-reviewer`列为用户自行管理的文件系统skill位置。两个个人位置选择一个即可，不要同时安装。

### 项目安装

如果只希望一个项目发现该skill，请使用：

```text
<项目根目录>/.agents/skills/om-reviewer
```

只有在该skill适合项目的所有授权使用者时，才将该目录提交到项目仓库。不要把保密稿件放在skill目录附近。

## 使用Skill Installer安装

这是推荐方式。Skill Installer会直接下载公开GitHub仓库，必要时回退到Git。私有仓库需要已有Git凭据，或者适当配置的`GITHUB_TOKEN`或`GH_TOKEN`。安装器不会覆盖已经存在的目标目录。

由于本仓库的`SKILL.md`位于仓库根目录，因此仓库内路径为`.`，安装名称必须指定为`om-reviewer`。

### ChatGPT桌面应用中的Codex

1. 在ChatGPT桌面应用中打开Codex。
2. 新建一个任务。
3. 粘贴本仓库地址，并发送以下请求。

```text
请使用 $skill-installer 从这个GitHub仓库安装om-reviewer。
skill位于仓库根目录，请使用路径 . 并将安装名称设为om-reviewer。
```

4. Codex请求联网权限时进行确认。
5. 安装完成后新建任务。如果skill没有出现，请重启应用。
6. 可以在侧边栏的Skills中查看，或者使用`$om-reviewer`显式调用。

### Codex CLI

启动Codex，然后发送相同的安装请求。

```text
$skill-installer

请从https://github.com/anan-915/om-reviewer.git安装om-reviewer。
skill位于路径 .，安装名称必须为om-reviewer。
```

安装完成后开启新的Codex会话。使用`/skills`检查是否已发现，或者在提示中输入`$om-reviewer`。

熟悉命令行的用户也可以直接调用内置安装脚本。

Windows PowerShell

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$installerPath = Join-Path $codexHomePath "skills\.system\skill-installer\scripts\install-skill-from-github.py"
python $installerPath --repo "anan-915/om-reviewer" --path "." --name "om-reviewer"
```

macOS或Linux

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
python "$codex_home_path/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo "anan-915/om-reviewer" --path "." --name "om-reviewer"
```

### Codex IDE扩展

IDE扩展与Codex CLI使用相同的文件系统skill位置。

1. 在Codex任务中通过`$skill-installer`安装，或者使用上面的直接安装命令。
2. 安装完成后开启新的IDE聊天。
3. 使用`/skills`或输入`$om-reviewer`确认skill可用。
4. 如果没有检测到更新，请重启IDE或重新加载窗口。

## 使用Git手动安装

如果希望以后直接通过`git pull`更新，可以保留一份Git克隆。

### Windows个人安装

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$skillsPath = Join-Path $codexHomePath "skills"
New-Item -ItemType Directory -Force -Path $skillsPath | Out-Null
git clone https://github.com/anan-915/om-reviewer.git (Join-Path $skillsPath "om-reviewer")
```

### macOS或Linux个人安装

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_home_path/skills"
git clone https://github.com/anan-915/om-reviewer.git "$codex_home_path/skills/om-reviewer"
```

### 当前项目安装

在目标项目根目录中执行：

```bash
mkdir -p .agents/skills
git clone https://github.com/anan-915/om-reviewer.git .agents/skills/om-reviewer
```

如果skill没有立即出现，请重启Codex或开启新的会话。

## 更新方法

更新方式必须与最初的安装方式相匹配。

### 更新Git克隆

Windows PowerShell

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
git -C (Join-Path $codexHomePath "skills\om-reviewer") pull --ff-only
```

macOS或Linux

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
git -C "$codex_home_path/skills/om-reviewer" pull --ff-only
```

项目安装可以在项目根目录执行`git -C .agents/skills/om-reviewer pull --ff-only`。

不要直接修改用于安装的Git克隆。需要开发或定制时，请使用独立fork或工作副本，确保`git pull --ff-only`能够稳定更新。

### 更新Skill Installer或复制安装

内置Skill Installer在目标目录已经存在时会停止，不会原地覆盖更新。

1. 将已安装的`om-reviewer`完整移动到所有skill发现目录之外，作为临时备份。
2. 使用相同的仓库、路径`.`和名称`om-reviewer`重新运行Skill Installer。
3. 开启新的Codex任务，并使用非保密材料进行测试。
4. 确认新版本正常后再删除备份。

应替换整个目录，而不是把新文件覆盖到旧目录中。这样可以防止上游已删除的文件继续残留并被使用。

## 验证安装

1. 确认安装目录包含`SKILL.md`、`references`、`scripts`、`assets`和`agents/openai.yaml`。
2. 新建Codex任务或重启Codex。
3. 在支持的界面使用`/skills`，或者输入`$om-reviewer`。
4. 首次测试应使用人工构造或非保密稿件。
5. 如果需要生成DOCX，请确认以下命令能够加载。

```powershell
python scripts/validate_review_output.py --help
python scripts/build_review_docx.py --help
```

独立文件系统skill可以用于ChatGPT桌面应用中的Codex、Codex CLI和Codex IDE扩展。独立GitHub skill不能直接安装到普通ChatGPT网页或移动端聊天中。如需支持这些界面，需要采用插件等其他受支持的打包方式。

## 使用方法

使用`$om-reviewer`显式调用skill，附上PDF或DOCX稿件，并在已知时说明目标期刊、审稿轮次和倾向性结论。

```text
使用 $om-reviewer 按SCI一区标准审查这篇稿件。
这是初审，我目前倾向于大修。
```

用户指定的结论用于控制报告方向，但不能改变事实或制造证据。如果稿件证据与指定结论明显冲突，skill会明确提示这种不一致。

使用随附脚本验证结构化结果并生成作者可见的DOCX：

```powershell
python scripts/validate_review_output.py review.json --strict
python scripts/build_review_docx.py review.json review-report.docx
```

DOCX生成脚本默认使用`assets/review-report-template.docx`。

## 保密与负责任使用

- 所有未公开稿件、补充材料、作者回复信和审稿报告均应作为保密材料处理。
- 不要在公开检索中使用未公开标题、作者姓名、独特研究主张或稿件原文。
- 不要把稿件、审稿报告、生成意见、提取文本或临时渲染文件提交到本仓库。
- 使用AI辅助审稿前，应检查期刊、出版商、机构和审稿协议的规定。相关政策禁止使用AI时，不应使用本skill进行实质性审稿。
- Skill的输出仅为审稿建议，最终出版决定由编辑作出。
- 只能谨慎报告可观察的研究诚信风险，证据不足时不得断言存在不端行为。

本仓库明确排除私人开发和校准过程中使用的历史审稿报告，不发布任何未公开稿件或可识别的审稿意见。

## 局限性

- 本skill不能替代领域判断、独立统计评估、法律意见、伦理审查或编辑决定。
- 输出质量取决于稿件文件是否完整且可读。
- 创新性和政策相关判断可能需要通过最新权威来源核验。
- 方法参考提供的是审查信号，而不是自动阈值或自动裁决。

## 致谢

本项目在开发过程中参考学习了[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)公开分享的skill设计、目录组织和分发实践。感谢袁一哲及该项目的贡献者为科研和开源社区分享相关工作。

`om-reviewer`为独立开发项目，不复制或重新分发其他项目的私人来源材料、稿件数据或项目专属内容。

## 许可证

本项目采用Apache License 2.0，详见[LICENSE](LICENSE)。

## 独立声明

这是一个独立项目，与OpenAI、Elsevier、任何期刊或出版商不存在隶属、认可或官方产品关系。项目中对外部指南和项目的引用仅用于标明公开资源，不代表相关机构认可本项目。

关于Codex当前的skill目录与调用方式，请参阅[OpenAI官方文档](https://learn.chatgpt.com/zh-Hans/docs/build-skills)。
