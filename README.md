# usability-evaluation-report

UX 用户体验评估报告 / 可用性测试报告生成 skill。把研究员**已收集、已聚类**的测试材料,整理成长滚动叙事式的交互 HTML 报告 + 独立的中间态 markdown 卡片清单。

> 一句话定位:**你是在把研究员的输入整理成报告,不是自己做研究。** 所有事实性内容都必须可追溯到输入,缺的标"待补充",绝不编造。

## 已确认报告与版本管理

当前确认版：**2026-11-16 / report-kunpeng-20261116-v1.0**，用户已确认内容及补图结果。

- [完整交互报告](kunpeng-ux-report-full.html)
- [完整卡片清单](kunpeng-ux-cards.md)
- [匿名数据及计算结果](kunpeng-ux-data.json)
- [生成与校验说明](kunpeng-ux-validation.md)

根目录这些文件始终表示最新确认版；旧版本通过 Git 提交历史和版本标签回溯，不再保留带“claude with图片”等过时命名的平行版本。后续修改完成并确认后再提交，正式确认版打标签，避免仅覆盖文件而无法回退。

技能源文件位于 `usability-evaluation-report/`。D盘 wooooooork 项目的 `.agents/skills/usability-evaluation-report` 连接到该技能源目录，共用同一份修改。

本报告包含28屏、19条观点、8条严重问题深挖；UI单题满意度9.00、八维综合均分9.46。内嵌8处截图，文档及社区的4处缺图继续占位。数据、匿名信息和静态结构检查已完成；浏览器视觉与点击交互未完成工具验收。

## 在大 skill 体系中的位置

UX 评估完整工作流的**第三个组件**,与上游两个 skill 产物对接,自己不做聚类、不做测试套件生产:

```
usability-evaluation-materials      →  usability-testing-interview-analysis  →  【本 skill】
   (测试套件:任务书/问卷/提纲)         (原声逐字稿 → 聚类观点 JSON)            (报告产出)
```

三者由总入口 `usability-evaluation-suite` 统一调度,用户无需手动按序调用。

## 何时使用 / 不应触发

**使用**:用户做完测试、有聚类后的观点 JSON/Excel,要整理成正式报告。

**不触发**:用户只有原声逐字稿(→ 先用 `usability-testing-interview-analysis` 聚类);问怎么聚类(→ analysis skill);问怎么设计测试任务(→ materials skill)。

## 输入与输出

**输入**——硬门槛 1 类 + 辅助 4 类:

| 类型 | 必需性 | 缺失处理 |
|---|---|---|
| 观点聚类文件(JSON / Excel) | **硬门槛** | 缺则拒绝,引导先走观点聚类 skill |
| 用户信息(被试画像) | 辅助 | 可反推,不能反推标"待补充" |
| 任务书 | 辅助 | 可从聚类文件的任务名反推 |
| 问卷结果 | 辅助 | 缺则相关指标标"待补充" |
| 观察记录(完成率/出错/时长) | 辅助 | 缺则标"未采集",仍保留指标位 |

**输出**——主报告与卡片为基本交付物；有较多数据时同时交付匿名数据JSON。输出路径使用当前环境约定的可交付目录（本项目为 D 盘项目的 `outputs/`；原容器环境可使用 `/mnt/user-data/outputs/`）：

| 产出 | 文件名 |
|---|---|
| 主报告(完整 / 重点摘要 / 自定义筛选) | `{项目名}-ux-report-{粒度}.html` |
| 中间态卡片(独立交付物) | `{项目名}-ux-cards.md` |
| 管理层一页纸(可选) | `{项目名}-ux-summary-exec.html` |
| 研发清单(可选) | `{项目名}-ux-issues-eng.html` |

> 报告里的真实截图/照片默认 base64 内嵌进单文件 HTML;**图很多或单图过大**时退化为 `HTML + 同级 images/ 文件夹`(放弃单文件、相对路径引用),整套打包交付。

## 五步工作流

| 步骤 | 做什么 | 主要查阅 |
|---|---|---|
| 1 启动 | 确认风格(v3/v4)+ 业务类型(ToB/ToC/ToD)+ 材料盘点,查启动门槛 | `dialog-scripts` `design-tokens` `business-type-variants` `edge-cases` |
| 2 校验 | 校验聚类文件;非聚类材料(原声/未聚类原始表)直接拒绝 | `input-schema` `dialog-scripts` |
| 3 粒度确认 | 默认只问报告类型;附加产物/筛选按需展开 | `dialog-scripts` `report-structure` |
| 4 中间态 & 确认 | **核心环节**:一次性出全部卡片(含图槽 ID + 文末图片清单),收图与离线回传也在此步,用户审完确认再渲染 | `card-templates` `dialog-scripts` |
| 5 渲染输出 | 以确认后的卡片为内容版本依据、匿名计算数据为指标依据渲染 HTML + 卡片 md + 可选附加产物;图按清单出图/缺图占位 | `report-structure` `input-schema` `card-templates` `design-tokens` `screen-layouts` `interaction-patterns` `visualization-patterns` 等 |

## 文件结构

| 文件 | 作用 | 何时读/运行 |
|---|---|---|
| `SKILL.md` | 主流程、职责边界、审核与引用要求 | 每次使用 |
| `reference/data-calculation.md` | 指标公式、有效样本、缺失处理、U编号脱敏、两位精度、附录明细 | 收到问卷或准备数据卡片时 |
| `scripts/calculate_metrics.py` | 按明确题目映射计算满意度与NPS | 生成问卷指标时 |
| `scripts/test_calculate_metrics.py` | 已知答案、缺失/越界、重复ID、舍入等回归测试 | 修改计算逻辑或迁移环境后 |
| `reference/dialog-scripts.md` | 启动、确认、材料提示等话术 | 对应交流步骤 |
| `reference/input-schema.md` | 聚类JSON/Excel解析与字段映射 | 输入校验 |
| `reference/report-structure.md` | 章节、SO WHAT、引用、附录和衍生产物 | 卡片组织与渲染 |
| `reference/card-templates.md` | 九种卡片及图槽、图片清单 | 卡片生成 |
| `reference/design-tokens.md` | v3/v4视觉样式 | 风格选择与渲染 |
| `reference/screen-layouts.md` | 版式、图片嵌入与降级 | 渲染 |
| `reference/interaction-patterns.md` | 导航、筛选、展开与悬停 | 渲染 |
| `reference/visualization-patterns.md` | 图表比例、同源数据与校验规则 | 渲染与交付检查 |
| `reference/business-type-variants.md` | ToB/ToC/ToD差异 | 业务类型取舍 |
| `reference/edge-cases.md` | 缺失、反推、样本与异常边界 | 遇到异常时 |
| `reference/sample-clustering.json` / `.xlsx` | 聚类输入样例 | 需要参考输入格式时 |
| `reference/sample-mockup-v4.html` / `sample-mockup.html` | v4/v3视觉样例，非项目数据基准 | 对应风格渲染时 |

## 设计原则

- **渐进式披露**:`SKILL.md` 只留每次都要在脑子里的骨架(原则、防幻觉、流程、gate、红线、指针),细节与逐字话术下沉到 `reference/`,执行到那一步再读。每个下沉块在原地留祈使式指针,弱模型不会在该读时找不到。
- **防幻觉为弱模型设计**:不依赖模型"自觉",靠 A(必须有据)/B(鼓励发挥)/C(渲染前自检)三组可照做的规则。
- **双输出**:HTML 给人看(可交互、可分发),卡片 markdown 给后续编辑/复用/归档——卡片是**平级交付物**,不是脚手架。
- **快照式**:每次基于当前全部材料重跑,不做增量;支持中期快照(被试未到齐时显式标注、措辞软化)。
- **职责单一**:只接受观点聚类文件,不做聚类、不做轻量降级,守住与上游 skill 的边界。
- **视觉一致**:全部报告用统一 design tokens(v3 公司 PPT 复刻 / v4 JetBrains 内化,默认 v4)。

## 安装、迁移与运行要求

迁移单位是整个 `usability-evaluation-report/` 技能目录，不是单独的 `SKILL.md`：

```text
usability-evaluation-report/
├── SKILL.md
├── README.md
├── reference/    # 公式、口径、脱敏、展示与输入输出规则
└── scripts/      # 指标计算程序与回归测试
```

- **规则与程序同时携带**：本次修改分别写在 `SKILL.md`、`reference/` 和 `scripts/`。reference提供可读规则，scripts负责确定性计算；不把计算逻辑只放在模型提示中。保留目录结构与相对路径，无需把脚本挪进reference。
- **目标环境**：须支持读取技能目录、执行本地代码并生成文件。当前计算脚本及测试只依赖Python 3标准库，无需额外安装数据计算包。问卷/文档/PDF读取和HTML视觉验收还需要目标环境提供相应工具；这些工具不随本技能打包。
- **运行位置**：下列命令从技能目录执行。输入问卷先按 `reference/data-calculation.md` 转成有明确题目映射的匿名JSON，不能把原始Excel直接传给脚本。

```sh
python scripts/calculate_metrics.py input.json output.json
python -B scripts/test_calculate_metrics.py
```

- **项目级使用**：将完整技能目录放入目标项目的 `.agents/skills/usability-evaluation-report/`，或显式指定其 `SKILL.md` 路径。当前D盘项目使用目录连接指向仓库源目录，避免两份副本漂移。
- **跨电脑**：Windows目录连接只在本机有效，不能把连接本身当作技能迁移；请复制连接指向的真实目录内容，或使用包含全部文件的压缩包。目标平台还需支持该技能格式，不能仅凭上传Markdown就保证脚本会执行。
- **代码运行不可用时**：先说明限制，不把模型心算结果声称为脚本计算。已有汇总值可引用并标注未复算；需要复算时待运行条件具备后继续。

## 最近更新

- **2026-11-17**：补充完整目录迁移方式、Python运行要求、脚本与reference分工，更新文件索引及输出目录说明。[完整变更记录](CHANGELOG.md)。
- **2026-11-16 / `1078532`**：明确满意度与NPS计算，U编号默认脱敏、均值两位小数、个人均分仅附录；加入计算脚本和回归测试，修正图表与输入边界冲突。
- **2026-11-16 / `54d70e3`**：归档用户确认的鲲鹏报告、匿名数据和校验说明，创建报告标签 `report-kunpeng-20261116-v1.0`；该标签不表示skill版本号。

## 维护 / 编辑约定

- 在仓库内修改技能并保留Git提交；按当前环境选择暂存与交付目录。可用skill-creator的 `quick_validate.py` 做结构校验；修改计算逻辑时运行技能自带回归测试。迁移或打包须包含整个技能目录。
- **改话术**只动 `dialog-scripts.md`;**改卡片结构**只动 `card-templates.md`;**改边界/反推/中期口径**只动 `edge-cases.md`——主体 `SKILL.md` 一般只在流程或红线变化时才动。
- 新增下沉内容时,务必在 `SKILL.md` 原地留指针,并同步更新「参考资源」索引。

## 变更记录

- **配图机制(图槽 + 文末图片清单)**:报告中的真实截图/照片改为"图槽 ID(写卡片正文)+ 文末「图片清单」表(描述唯一来源 + 渲染索引,不作为报告一屏)"。收图时机从"渲染后"前移到**步骤 4 卡片确认时**;绑定按模型能力分流(看图自动绑 / 按图槽 ID 命名文件机械匹配 / 用户手填),对用户话术通俗化;缺图渲占位标"待补充"绝不编造;新增"图多/图大"逃生通道(降采样 或 HTML+images 文件夹)。卡片 md 支持**离线编辑后回传**,渲染以回传版为内容版本依据，数字与匿名计算数据核对并做轻量对账。涉及 `SKILL.md`、`card-templates.md`、`screen-layouts.md`、`dialog-scripts.md`、`report-structure.md`。
- **本次重构**:`SKILL.md` 599 → 372 行。新建 `dialog-scripts.md` 收纳全部对用户话术;卡片结构、v3/v4 差异表、版式/紧凑/图片占位、校验字段细节、中期口径分别下沉到既有 reference;主体只留逻辑与指针。骨架(核心原则 / 防幻觉 A·B·C / 工作流 / 启动门槛 / 红线)保持不变。
- **封面标题规则**:`report-structure.md` 屏 0.0 明确「H1 主标题 = 报告主题(产品名 + 评估类型),不用结论句;结论降级为副标题或并入 TL;DR」,防止把卡片的核心观点误渲染成主标题。

## 数据准确性更新

新增 `reference/data-calculation.md` 与 `scripts/calculate_metrics.py`：明确整体满意度单题、各维度得分、体验维度综合均分与 NPS 口径，按各题有效样本计算，均值两位小数；默认 U 编号脱敏，个人维度均分仅放附录。图表与文字读取同一数据，交付前验证比例尺与图数一致性。
