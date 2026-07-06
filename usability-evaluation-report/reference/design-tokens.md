# Design Tokens

报告渲染时强制使用统一的设计 token 体系,确保多份报告视觉一致。

本文件维护**两套并行的视觉风格**,两版的来源不同:

- **v3 风格(公司 PPT 模板复刻)**:按公司既有 PPT 模板的章节结构和配色 1:1 复刻 —— 深蓝主色 + 米白底 + 屏式长滚动。适合需要**与既有 PPT 视觉延续**的场景(严肃汇报、对外正式版本、跟线下材料配套发布)。
- **v4 风格(JetBrains 设计语言内化)**:基于 JetBrains 官网/产品页/年度报告的视觉系统内化重构 —— 多彩当代色 + Geist/JetBrains Mono 字体 + 12 列卡片网格 + SO WHAT/TL;DR 强结论块。适合**独立网页呈现**的场景(内部观察、迭代追踪、希望"一目了然"扫读)。

渲染前先在 SKILL.md 步骤 1 之前(可作为"步骤 0")和用户确认要用哪一套。**默认 v4**(更适合"一目了然"的现代数据呈现需求)。

> **重要**:严重程度字面值**严格保留上游 input-schema 的原值**:`致命 / 严重 / 一般 / 提示`。
> 不要替换为"危急 / 严重 / 中等 / 轻微"。颜色映射按表对应,文字不变。

---

## v3 风格 token(公司 PPT 模板复刻)

### CSS 变量定义

```css
:root {
  /* ===== 背景 ===== */
  --bg: #fafaf8;
  --bg-alt: #f3f2ed;
  --bg-card: #ffffff;

  /* ===== 文字 ===== */
  --text: #1a1a1a;
  --text-2: #5a5a55;
  --text-3: #8e8e88;

  /* ===== 边框 ===== */
  --line: rgba(0,0,0,0.08);
  --line-2: rgba(0,0,0,0.15);

  /* ===== 主色 ===== */
  --accent: #2d4a6b;
  --accent-soft: #e8eef5;

  /* ===== 严重程度语义色 ===== */
  --sev-fatal: #8b2d2d;        /* 致命 */
  --sev-fatal-soft: #f5e6e6;
  --sev-serious: #8a5a1a;      /* 严重 */
  --sev-serious-soft: #f5ecdc;
  --sev-normal: #2d4a6b;       /* 一般 (与 accent 同) */
  --sev-normal-soft: #e8eef5;
  --sev-hint: #8e8e88;         /* 提示 */
  --sev-hint-soft: #f3f2ed;

  /* 别名 - 兼容性 */
  --danger: var(--sev-fatal);
  --danger-soft: var(--sev-fatal-soft);
  --warning: var(--sev-serious);
  --warning-soft: var(--sev-serious-soft);
  --info: var(--sev-normal);
  --info-soft: var(--sev-normal-soft);
  --success: #2d5a3a;
  --success-soft: #e6efe9;

  /* ===== 字体 ===== */
  --font: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
  --font-serif: "Songti SC", "STSong", Georgia, serif;
  --font-mono: "SF Mono", Menlo, Consolas, monospace;
}
```

### v3 字号体系

| 用途 | 字号 | 字重 |
|---|---|---|
| 报告主标题(封面) | 48px | 500 |
| 章节扉页大标题 | 40px | 500 |
| 屏标题 | 24px | 500 |
| 区块小标题 | 14px | 500 |
| 正文 | 14-15px | 400 |
| 元信息 | 13px | 400 |
| 数据来源、时间戳 | 11-12px | 400 (mono) |
| 大数字(KPI) | 36-40px | 500 |

---

## v4 风格 token(JetBrains 设计语言内化)

### 字体加载(必须放在 HTML `<head>` 顶部)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
```

**降级策略**:`display=swap` 保证 Google Fonts 加载失败或慢时,页面立刻用 fallback 渲染,不白屏。`--font-sans` 中的 fallback 链已包含 Inter / 系统字体 / 苹方 / 微软雅黑,极端内网环境也不会崩,只是丢失 Geist 的独特感。

### CSS 变量定义

```css
:root {
  /* ===== 背景 ===== */
  --bg: #FAFAFB;
  --bg-card: #FFFFFF;
  --bg-subtle: #F2F2F4;
  --bg-tag: #EEEEF0;

  /* ===== 文字 ===== */
  --ink: #0A0A0A;
  --ink-2: #1F1F23;
  --ink-soft: #525258;
  --ink-faint: #8B8B91;

  /* ===== 边框 ===== */
  --line: #E5E5E8;
  --line-strong: #0A0A0A;

  /* ===== 多彩调色板(图表与强调) ===== */
  --c-mint: #00C896;
  --c-coral: #FF6B6B;
  --c-blue: #3B82F6;
  --c-amber: #FFB800;
  --c-violet: #8B5CF6;
  --c-pink: #EC4899;

  /* 配套柔和色 */
  --c-mint-soft: #D1F4E7;
  --c-coral-soft: #FFD9D9;
  --c-blue-soft: #DBEAFE;
  --c-amber-soft: #FFEFC2;
  --c-violet-soft: #EDE3FE;

  /* SO WHAT 关键结论卡专用 */
  --callout-bg: #FFFBEC;
  --callout-border: #F5E6B8;
  --callout-key-hl: #FFE19E;

  /* ===== 严重程度语义色 - 对齐 input-schema 4 档字面值 ===== */
  --sev-fatal: #DC2626;         /* 致命 (上游 schema 第 1 档) */
  --sev-fatal-soft: #FEE2E2;
  --sev-serious: #EA580C;       /* 严重 (上游 schema 第 2 档) */
  --sev-serious-soft: #FFEDD5;
  --sev-normal: #3B82F6;        /* 一般 (上游 schema 第 3 档) */
  --sev-normal-soft: #DBEAFE;
  --sev-hint: #8B8B91;          /* 提示 (上游 schema 第 4 档) */
  --sev-hint-soft: #F2F2F4;

  /* 别名 - 兼容旧代码与通用语义 */
  --danger: var(--sev-fatal);
  --danger-soft: var(--sev-fatal-soft);
  --warning: var(--sev-serious);
  --warning-soft: var(--sev-serious-soft);
  --info: var(--sev-normal);
  --info-soft: var(--sev-normal-soft);
  --success: #16A34A;            /* 已接纳 */
  --success-soft: #DCFCE7;

  /* ===== 字体 ===== */
  --font-sans: 'Geist', 'Inter', -apple-system, BlinkMacSystemFont, "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
}
```

### v4 字号体系

| 用途 | 字号 | 字重 | 字体 |
|---|---|---|---|
| 报告主标题(hero) | clamp(36px, 5vw, 64px) | 600 | sans |
| 章节扉页大标题 | 40-48px | 600 | sans |
| 屏标题(section-title) | 24px | 600 | sans |
| 卡片标题(card-title) | 16px | 500 | sans |
| 卡片标签(card-label) | 11px | 400 | mono |
| 正文 | 14-15px | 400 | sans |
| 元信息 / Tag / 时间戳 | 11-12px | 500 | mono |
| 大数字(stat-num) | 44-64px | 500 | sans |
| Hero 横排 stat | 44px | 500 | sans |
| TL;DR 结论文字 | 16px | 500 | sans |
| SO WHAT 结论文字 | 17px | 500 | sans |
| 问题全局 ID | 0.7em (相对标题) | 500 | mono |

**关键差异 vs v3**:
- v4 标题字重普遍 **600**(v3 是 500),配合 Geist 的现代轮廓更清晰
- 大数字使用 sans 而非 mono(数字字号大时 sans 更现代)
- mono 字体仅用于:tag / 时间戳 / 编号 / 数据来源标注 / 问题 ID

### v4 间距体系

| 用途 | 数值 |
|---|---|
| 屏 / Section 内边距 | `padding: 64px 32px` (主区) / `padding: 100px 32px` (hero) |
| 12 列网格容器 | `max-width: 1400px; margin: 0 auto` |
| 卡片网格 gap | `gap: 16px` |
| 卡片内边距 | `padding: 24px` (普通) / `padding: 32px 36px` (TL;DR / SO WHAT) |

### v4 圆角

| 元素 | 圆角值 |
|---|---|
| 普通卡片 | 8px |
| TL;DR / SO WHAT 大卡 | 8-12px |
| Tag / pill / button / chip | 4-6px |
| 进度条 / bar fill | 4px |

---

## 跨版本通用约定

### 严重程度颜色语义(v3 / v4 都遵守)

**字面值严格对齐 input-schema** —— 直接使用上游原值,不做术语替换:

| 上游字面值 | 文字色 token | 背景色 token | chip className |
|---|---|---|---|
| **致命** | `var(--sev-fatal)` | `var(--sev-fatal-soft)` | `.severity-chip.is-fatal` |
| **严重** | `var(--sev-serious)` | `var(--sev-serious-soft)` | `.severity-chip.is-serious` |
| **一般** | `var(--sev-normal)` | `var(--sev-normal-soft)` | `.severity-chip.is-normal` |
| **提示** | `var(--sev-hint)` | `var(--sev-hint-soft)` | `.severity-chip.is-hint` |

### 优先级(对应严重程度)

| 优先级 | 颜色 token |
|---|---|
| P0 | `var(--sev-fatal)` |
| P1 | `var(--sev-serious)` |
| P2 | `var(--sev-normal)` (v4) / `var(--text-2)` (v3) |
| P3 | `var(--sev-hint)` |

### 接纳状态

| 状态 | 颜色 |
|---|---|
| 已接纳 | `var(--success)` |
| 评估中 | `var(--c-blue)` (v4) / `var(--text-3)` (v3) |
| 未接纳 | `var(--ink-faint)` (v4) / `var(--text-3)` (v3) |

### 问题类型 chip(5 类固定枚举)

来自 input-schema,**全部用 neutral 灰色 chip**,不为每类指定独立颜色——避免类型枚举扩展时颜色不够用:

```css
.type-chip {
  display: inline-flex;
  font-family: var(--font-mono);
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 4px;
  background: var(--bg-tag);     /* v4 用 #EEEEF0 */
  color: var(--ink-soft);
}
```

5 类枚举:`信息设计类` / `产品功能类` / `视觉设计类` / `业务流程类` / `客户服务类`。

**例外**:在"问题类型分布"图表中允许用多色区分(图表语义),但 chip 始终用 neutral 灰。

---

## v4 专属组件:关键结论 / SO WHAT 卡

每个章节末尾的"强结论"区块。

### 视觉规范

```css
.so-what {
  background: var(--callout-bg);
  color: var(--ink);
  border: 1px solid var(--callout-border);
  border-left: 4px solid var(--c-amber);
  border-radius: 8px;
  padding: 22px 26px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 24px;
}

.so-what-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--ink-faint);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 8px;
}

.so-what-tag::before {
  content: '';
  width: 6px; height: 6px;
  background: var(--c-amber);
  border-radius: 50%;
}

.so-what-text {
  font-size: 17px;
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.45;
}

.so-what-text .key {
  background: linear-gradient(180deg, transparent 60%, var(--callout-key-hl) 60%);
  font-weight: 600;
  padding: 0 3px;
}
```

### 使用规则

- 每个章节末尾**最多一张** SO WHAT 卡
- `.key` 高亮**每段最多 2 处**,过多就稀释重点
- 文字简短(中文 ≤ 50 字)
- 文字内容是"结论 + 行动指向",不是数据复述

### 替代场景:note-card

如果一段结论太长(或属性更接近"研究笔记"而非"so what"),用普通 note-card:

```css
.note-card {
  background: var(--bg-subtle);
  border-radius: 6px;
  padding: 16px 18px;
  font-size: 13px;
  color: var(--ink-soft);
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px;
  align-items: center;
}
.note-card .note-tag {
  font-family: var(--font-mono);
  font-size: 10px;
  background: var(--ink);
  color: white;
  padding: 4px 8px;
  border-radius: 3px;
  letter-spacing: 0.05em;
  font-weight: 500;
  white-space: nowrap;
  align-self: start;
  margin-top: 1px;
}
```

适合放"研究笔记 / 数据备注 / 深访洞察 / 验收标准"——比 so-what 弱一档的次级强调。

---

## v4 专属组件:Hero stat strip

封面顶部的"4 项关键数字横排"模块。

```css
.hero-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-top: 1px solid var(--line-strong);
  border-bottom: 1px solid var(--line-strong);
}

.hero-strip-item {
  padding: 24px;
  border-right: 1px solid var(--line);
}
.hero-strip-item:last-child { border-right: none; }

.strip-num {
  font-size: 44px;
  font-weight: 500;
  letter-spacing: -0.03em;
}

/* 严重相关数字用 sev token 配色 */
.strip-num.is-fatal { color: var(--sev-fatal); }     /* 例:问题总数 = 23 */
.strip-num.is-mint { color: var(--c-mint); }         /* 例:需求总数 (正面) */
.strip-num.is-amber { color: var(--c-amber); }       /* 例:整体满意度 */
.strip-num.is-coral { color: var(--c-coral); }       /* 例:完成率(低) */

.strip-trend.up { color: var(--c-mint); }
.strip-trend.down { color: var(--c-coral); }
.strip-trend.flat { color: var(--ink-faint); }
```

### 使用规则

- **4 项**最佳,3 项可接受
- 数字下方必须配:**descriptor**(数字代表什么)+ **trend**(同比/环比 或 "首次度量")
- 趋势箭头 `↑` `↓` `—`,数字符号统一 `+18pp`、`-3pp`

---

## v4 专属组件:TL;DR 卡

封面下方的"3 句话总结"卡。

### 视觉规范

```css
.tldr-card {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 32px 36px;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 36px;
}

.tldr-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  position: relative;
}
.tldr-list::before, .tldr-list::after {
  content: '';
  position: absolute;
  top: 0; bottom: 0;
  width: 1px;
  background: var(--line);
}
.tldr-list::before { left: 33.33%; }
.tldr-list::after { left: 66.66%; }

.tldr-item .n::before {
  content: '';
  width: 18px;
  height: 2px;
  background: var(--c-amber);
  display: inline-block;
  margin-right: 8px;
}

.tldr-item .t strong {
  background: linear-gradient(180deg, transparent 60%, var(--callout-key-hl) 60%);
  font-weight: 600;
}
```

### 使用规则

- 必须 **3 条**(报告级核心结论 = 3 句话讲清)
- 每条 ≤ 25 字,关键词用 `<strong>` 包裹
- TL;DR 只在第 2 章前面(整体结论之前),不出现在其他位置

---

## v4 专属组件:Issue header (问题深挖头)

承担"全局 ID + 观点标签 + 严重程度 + 问题类型 + 影响人数"的展示责任,严格对齐 input-schema 字段映射。

```html
<div class="issue-header">
  <h3 class="issue-title">
    <span class="global-id">P-001</span>导航分类不够直观
  </h3>
  <span class="severity-chip is-fatal">致命</span>
  <span class="type-chip">信息设计类</span>
  <span class="severity-chip is-soft">影响 8/12 被试</span>
</div>
```

```css
.issue-title .global-id {
  font-family: var(--font-mono);
  font-size: 0.7em;
  font-weight: 500;
  color: var(--ink-faint);
  margin-right: 8px;
}
```

字段来源:

| 显示内容 | 来源 |
|---|---|
| `P-001` | input-schema 中按"严重程度排序"生成的全局 ID |
| `导航分类不够直观` | 观点对象的 `观点标签` 字段 |
| `致命` | 观点对象的 `严重程度` 字段(原值不替换) |
| `信息设计类` | 观点对象的 `问题类型` 字段 |
| `8/12` | 观点对象的 `用户数` / 总样本数 |

### 元信息条规范

```html
<div class="issue-meta-row">
  <div class="issue-meta-item">
    <span class="label">本地溯源 ID</span>
    <span class="value mono">T1-OP1</span>
  </div>
  ...
</div>
```

必含字段:
- **本地溯源 ID**(`T{任务序号}-OP{观点序号}`,来自 schema)
- **关联任务**(任务序号 + 任务名称简略)
- **问题类型**(5 类枚举之一)
- **用户数 / 总样本**(从观点对象的 `用户数` 字段 + 全局样本数)
- **业务方状态**(用户后期补充的)

---

## v4 多彩色板使用规则

v4 有 5+ 种强调色,容易滥用。规则:

| 色 | 主要用途 | 不要用于 |
|---|---|---|
| **mint 薄荷绿** | 增长趋势、正面数据、主要发现、需求(正面) | 警示、问题 |
| **coral 珊瑚粉** | 焦虑、负面情绪、问题相关 | 庆祝类 |
| **blue 天蓝** | 中性主体、链接、说明性数据、"评估中"状态 | 强调最重要的结论 |
| **amber 琥珀黄** | 关键结论、SO WHAT、TL;DR、最重要的强调 | 普通数据 |
| **violet 紫色** | 引语 / 辅助信息 / 较弱强调 | 主要数据 |
| **pink 备用** | 罕用,仅作 6 类分类时的第 6 色 | 强调 |

**严重程度颜色独立于多彩调色板** —— sev-fatal/serious/normal/hint 是专门的语义色,不要混用普通的 mint/coral 来标记严重程度。

**单屏配色规则**:一屏内最多用 3-4 种颜色,超过就视觉过载。

---

## v3 / v4 共通:阴影、动画

### 阴影(克制使用)

```css
/* 卡片悬停浮起 */
box-shadow: 0 2px 8px rgba(10,10,10,0.06);   /* v4 用近黑阴影 */
box-shadow: 0 2px 8px rgba(45,74,107,0.08);  /* v3 用主色阴影 */

/* 顶部 sticky nav 模糊背景 */
background: rgba(250, 250, 251, 0.85);
backdrop-filter: blur(12px);
```

### 动画

| 元素 | 过渡 |
|---|---|
| 卡片悬停 | `transition: all 0.15s` |
| 进度条 fill | `transition: width 1s cubic-bezier(0.2, 0.8, 0.2, 1)` |

---

## 选哪个版本?快速判断

**核心判断:这份报告的发布场景与谁对齐?**
- 跟公司既有 PPT/汇报材料配套 → **v3**(PPT 模板复刻,视觉延续)
- 独立网页/飞书/Notion 呈现 → **v4**(JetBrains 设计语言,独立扫读)

| 场景 | 推荐 |
|---|---|
| 想跟公司既有 PPT 视觉延续 | **v3** |
| 给业务方季度汇报 / 高层 | v3(沉稳)或 v4(看业务方调性) |
| 团队内部观察 / 月度迭代追踪 | **v4**(明亮、扫读) |
| 严肃 ToB 产品 / 政府客户 | v3(稳重) |
| 创新产品 / AI / 工具类 / 年轻消费品 | **v4** |
| 用户希望"一目了然" / "现代数据感" | **v4** |
| 用户希望"杂志感" / "深度阅读" | v3 |

**默认 v4**。在步骤 1 让用户确认。

## v3 / v4 差异速查 + 设计来源

**两版的设计来源不同,不只是 token 不同**:

- **v3** 来自**公司既有 PPT 模板**的 1:1 复刻 —— 章节结构、配色、版式都对齐公司线下汇报材料,目的是"线上线下视觉延续"。
- **v4** 是**对 JetBrains 设计语言的内化重构** —— 卡片网格、Geist 字体、SO WHAT 强结论块、Hero stat strip 等模式来自 JetBrains 官网/产品页/年度报告的视觉系统,在本场景下做了 UX 报告的适配。

因此选型时不只看"好不好看",更要看**这份报告的发布场景与谁对齐**(详见上节「选哪个版本」)。

| 维度 | v3 | v4 |
|---|---|---|
| 主色板 | 深蓝 #2d4a6b 单色 | 多彩(mint/coral/blue/amber/violet) |
| 字体 | 系统字体 | Geist + JetBrains Mono(需引入 Google Fonts) |
| 底色 | 米白 #fafaf8 | 浅灰白 #FAFAFB |
| 主体布局 | 屏式长滚动 | 12 列卡片网格 |
| 关键结论 | 结论横幅 | SO WHAT 卡(淡琥珀底 + 关键词高亮) |
| 全局摘要 | 无 | TL;DR 卡(3 句话) |
| 顶部数据 | 仪表盘式 | Hero stat strip(4 项横排) |
| 严重程度色 | 深沉色 | 鲜亮色(更醒目) |
| 严重程度字面值 | **致命/严重/一般/提示** | **致命/严重/一般/提示** |
| 问题类型 chip | neutral 灰色 | neutral 灰色 |

**关键判断**:

- 选 v4 时,**必须**在 HTML `<head>` 里引入 Geist + JetBrains Mono 的 Google Fonts link。
- 选 v4 时,数据展示**优先用卡片网格**(`.card-grid` 12 列),而非 v3 的"一屏一事"长滚动。
- 严重程度字面值在两版都用上游 schema 原值(`致命/严重/一般/提示`),**不要替换**。
- 严重程度的语义色 token 都叫 `--sev-fatal` / `--sev-serious` / `--sev-normal` / `--sev-hint`,语义不变,仅色值不同。
