# usability-evaluation-report

UX 用户体验评估报告 / 可用性测试报告生成 skill。把研究员**已收集、已聚类**的测试材料,整理成长滚动叙事式的交互 HTML 报告 + 独立的中间态 markdown 卡片清单。

> 一句话定位:**你是在把研究员的输入整理成报告,不是自己做研究。** 所有事实性内容都必须可追溯到输入,缺的标"待补充",绝不编造。

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

**输出**——每次至少 2 件,放 `/mnt/user-data/outputs/`:

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
| 5 渲染输出 | 以(可能回传的)卡片 md 为唯一来源渲染 HTML + 卡片 md + 可选附加产物;图按清单出图/缺图占位 | `report-structure` `input-schema` `card-templates` `design-tokens` `screen-layouts` `interaction-patterns` `visualization-patterns` 等 |

## 文件结构

| 文件 | 行数 | 作用 | 何时读 |
|---|---|---|---|
| `SKILL.md` | 389 | 主流程 + 判断逻辑 + 红线 | 每次必读(常驻) |
| `reference/dialog-scripts.md` | 108 | 全部对用户的交流话术 | 对用户开口时 |
| `reference/input-schema.md` | 424 | 聚类文件 JSON/Excel 解析 schema | 步骤 2 + 渲染前 |
| `reference/report-structure.md` | 173 | 6 章屏级结构 + 封面标题规则 + SO WHAT + 引用 + 衍生产物 | 渲染前必读 |
| `reference/card-templates.md` | 241 | 卡片通用结构 + 9 类型样板 | 步骤 4 必读 |
| `reference/design-tokens.md` | 591 | v3/v4 双轨 token + 差异速查 + 选型 | 选型 + 渲染 |
| `reference/screen-layouts.md` | 323 | 版式模板 + 版式选择 + 紧凑度 + 图片渲染与降级 | 渲染 |
| `reference/interaction-patterns.md` | 267 | 锚点导航/筛选/tab/悬停 实现 | 渲染 |
| `reference/visualization-patterns.md` | 265 | 雷达/饼/条形/数字卡/接纳率 实现 | 渲染 |
| `reference/business-type-variants.md` | 184 | ToB/ToC/ToD 章节与维度差异 | 步骤 1.2 + 渲染 |
| `reference/edge-cases.md` | 78 | 缺失/反推/被试偏少/观点集中/中期口径 | 材料异常时先读 |
| `reference/sample-clustering.json` / `.xlsx` | — | 输入样例(两种形态) | 参考 |
| `reference/sample-mockup-v4.html`(默认)/ `sample-mockup.html`(v3) | — | 输出样例 | 渲染时二选一 |

## 设计原则

- **渐进式披露**:`SKILL.md` 只留每次都要在脑子里的骨架(原则、防幻觉、流程、gate、红线、指针),细节与逐字话术下沉到 `reference/`,执行到那一步再读。每个下沉块在原地留祈使式指针,弱模型不会在该读时找不到。
- **防幻觉为弱模型设计**:不依赖模型"自觉",靠 A(必须有据)/B(鼓励发挥)/C(渲染前自检)三组可照做的规则。
- **双输出**:HTML 给人看(可交互、可分发),卡片 markdown 给后续编辑/复用/归档——卡片是**平级交付物**,不是脚手架。
- **快照式**:每次基于当前全部材料重跑,不做增量;支持中期快照(被试未到齐时显式标注、措辞软化)。
- **职责单一**:只接受观点聚类文件,不做聚类、不做轻量降级,守住与上游 skill 的边界。
- **视觉一致**:全部报告用统一 design tokens(v3 公司 PPT 复刻 / v4 JetBrains 内化,默认 v4)。

## 维护 / 编辑约定

- 改 skill 在 `/tmp/` 暂存,`str_replace` 做定向编辑,`quick_validate.py` 校验、`package_skill.py` 打包成 `.skill`。
- **改话术**只动 `dialog-scripts.md`;**改卡片结构**只动 `card-templates.md`;**改边界/反推/中期口径**只动 `edge-cases.md`——主体 `SKILL.md` 一般只在流程或红线变化时才动。
- 新增下沉内容时,务必在 `SKILL.md` 原地留指针,并同步更新「参考资源」索引。

## 变更记录

- **配图机制(图槽 + 文末图片清单)**:报告中的真实截图/照片改为"图槽 ID(写卡片正文)+ 文末「图片清单」表(描述唯一来源 + 渲染索引,不作为报告一屏)"。收图时机从"渲染后"前移到**步骤 4 卡片确认时**;绑定按模型能力分流(看图自动绑 / 按图槽 ID 命名文件机械匹配 / 用户手填),对用户话术通俗化;缺图渲占位标"待补充"绝不编造;新增"图多/图大"逃生通道(降采样 或 HTML+images 文件夹)。卡片 md 支持**离线编辑后回传**,渲染以回传版为唯一事实来源并做轻量对账。涉及 `SKILL.md`、`card-templates.md`、`screen-layouts.md`、`dialog-scripts.md`、`report-structure.md`。
- **本次重构**:`SKILL.md` 599 → 372 行。新建 `dialog-scripts.md` 收纳全部对用户话术;卡片结构、v3/v4 差异表、版式/紧凑/图片占位、校验字段细节、中期口径分别下沉到既有 reference;主体只留逻辑与指针。骨架(核心原则 / 防幻觉 A·B·C / 工作流 / 启动门槛 / 红线)保持不变。
- **封面标题规则**:`report-structure.md` 屏 0.0 明确「H1 主标题 = 报告主题(产品名 + 评估类型),不用结论句;结论降级为副标题或并入 TL;DR」,防止把卡片的核心观点误渲染成主标题。
