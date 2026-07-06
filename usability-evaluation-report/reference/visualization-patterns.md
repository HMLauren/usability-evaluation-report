# Visualization Patterns

报告中常用的可视化图表实现。优先使用纯 SVG 或 CSS 实现,避免引入第三方库(单文件 HTML 原则)。

## 1. 维度均分雷达图

**用途**:整体测试结果总览(屏 2.1)。

**实现**:纯 SVG + 少量 JS 计算坐标。

### 代码模板

```html
<svg viewBox="-150 -150 300 300" width="100%" height="280">
  <!-- 同心多边形背景(4 层) -->
  <g fill="none" stroke="rgba(0,0,0,0.06)" stroke-width="0.5">
    <polygon id="ring1" points=""/>
    <polygon id="ring2" points=""/>
    <polygon id="ring3" points=""/>
    <polygon id="ring4" points=""/>
  </g>
  <!-- 数据多边形 -->
  <polygon id="data-poly" points="" fill="rgba(45,74,107,0.18)" stroke="#2d4a6b" stroke-width="1.5"/>
  <!-- 数据点(短板高亮) -->
  <g id="data-points"></g>
  <!-- 标签 -->
  <g id="labels" font-size="10" fill="#5a5a55"></g>
</svg>

<script>
(function renderRadar() {
  const dims = [
    {name:'易学性', value:8.3},
    {name:'效率', value:7.5},
    // ... 11 维度
  ];
  const N = dims.length;
  const R = 110;
  const angle = i => (Math.PI * 2 * i) / N - Math.PI / 2;

  // 同心环(4 层 25/50/75/100%)
  [0.25, 0.5, 0.75, 1].forEach((ratio, idx) => {
    const ring = document.getElementById('ring' + (idx + 1));
    let pts = '';
    for (let i = 0; i < N; i++) {
      const r = R * ratio;
      pts += (r * Math.cos(angle(i))) + ',' + (r * Math.sin(angle(i))) + ' ';
    }
    ring.setAttribute('points', pts.trim());
  });

  // 数据多边形
  let dataPts = '';
  dims.forEach((d, i) => {
    const r = (d.value / 10) * R;
    dataPts += (r * Math.cos(angle(i))) + ',' + (r * Math.sin(angle(i))) + ' ';
  });
  document.getElementById('data-poly').setAttribute('points', dataPts.trim());

  // 数据点(短板 ≤ 6.5 用 danger 色 + 大点)
  const pointsG = document.getElementById('data-points');
  dims.forEach((d, i) => {
    const r = (d.value / 10) * R;
    const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    c.setAttribute('cx', r * Math.cos(angle(i)));
    c.setAttribute('cy', r * Math.sin(angle(i)));
    c.setAttribute('r', d.value <= 6.5 ? 4 : 2.5);
    c.setAttribute('fill', d.value <= 6.5 ? '#8b2d2d' : '#2d4a6b');
    pointsG.appendChild(c);
  });

  // 标签
  const labelsG = document.getElementById('labels');
  dims.forEach((d, i) => {
    const labelR = R + 18;
    const x = labelR * Math.cos(angle(i));
    const y = labelR * Math.sin(angle(i));
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', x);
    t.setAttribute('y', y);
    t.setAttribute('text-anchor', x < -10 ? 'end' : (x > 10 ? 'start' : 'middle'));
    t.setAttribute('dominant-baseline', y < -10 ? 'auto' : (y > 10 ? 'hanging' : 'middle'));
    t.setAttribute('font-size', '10');
    t.setAttribute('fill', d.value <= 6.5 ? '#8b2d2d' : '#5a5a55');
    t.setAttribute('font-weight', d.value <= 6.5 ? '500' : '400');
    t.textContent = d.name + ' ' + d.value;
    labelsG.appendChild(t);
  });
})();
</script>
```

**短板阈值**:默认 ≤ 6.5(10 点量表)。模型可根据数据分布动态调整,例如所有维度都 ≥ 7 时,将阈值设为最低 2-3 个维度。

## 2. 饼图(donut)

**用途**:岗位分布、设备偏好等分类数据。

**实现**:纯 CSS `conic-gradient`。

```html
<div class="donut-wrap">
  <div class="donut" style="
    background: conic-gradient(
      #2d4a6b 0% 33%,
      #5a7a99 33% 58%,
      #8ba6c2 58% 83%,
      #d6dde4 83% 100%
    );
  "></div>
  <div class="donut-legend">
    <div class="item"><span class="dot" style="background:#2d4a6b"></span><span class="name">产品经理</span><span class="pct">33%</span></div>
    <!-- ... -->
  </div>
</div>
```

```css
.donut {
  width: 110px; height: 110px;
  border-radius: 50%;
  position: relative;
}
.donut::after {
  content: '';
  position: absolute;
  inset: 22px;
  background: var(--bg-card);
  border-radius: 50%;
}
```

**配色梯度**(从深到浅):`#2d4a6b → #5a7a99 → #8ba6c2 → #b3c2d4 → #d6dde4`

## 3. 横向条形图

**用途**:维度均分(简版,用于卡片内)、画像分布、任务表现。

```html
<div class="h-bar">
  <span class="name">熟练用户</span>
  <span class="track"><span class="fill" style="width:58%"></span></span>
  <span class="value">7</span>
</div>
```

```css
.h-bar {
  display: grid;
  grid-template-columns: 80px 1fr 32px;
  gap: 10px;
  align-items: center;
  font-size: 12px;
  margin-bottom: 6px;
}
.h-bar .track { height: 8px; background: var(--bg-alt); border-radius: 2px; overflow: hidden; }
.h-bar .fill { height: 100%; background: var(--accent); border-radius: 2px; transition: width 0.6s; }
```

**警示条**(短板 / 高风险):增加 `.warn` 类,`background: var(--danger)`。

## 4. 数据数字卡

**用途**:KPI 展示。

```html
<div class="stat-mini">
  <div class="num">12</div>
  <div class="label">被试总数</div>
  <div class="hint">线上 + 线下</div>
</div>
```

```css
.stat-mini {
  background: var(--bg-card);
  border: 0.5px solid var(--line);
  border-radius: 6px;
  padding: 16px 18px;
}
.stat-mini .num { font-size: 32px; font-weight: 500; line-height: 1; margin-bottom: 4px; }
.stat-mini .label { font-size: 12px; color: var(--text-2); }
.stat-mini .hint { font-size: 11px; color: var(--text-3); margin-top: 4px; }
```

**强调态**(突出某个数字):

```css
.stat-mini.accent {
  background: var(--accent-soft);
  border-color: var(--accent);
}
.stat-mini.accent .num { color: var(--accent); }
```

## 5. 进度条 / 接纳率

**用途**:问题/需求接纳率展示。

```html
<div class="accept-block accepted">
  <div class="label-ab">问题接纳率</div>
  <div class="num-ab">78<span class="pct">%</span></div>
  <div class="hint-ab">已接纳 18 / 23</div>
</div>
```

接纳率 ≥ 70% 用 `--success` 色,< 70% 用默认主色。

## 6. 任务卡

**用途**:任务概览。

```html
<div class="task-card danger">
  <span class="task-detail-arrow">→</span>
  <div class="task-card-head">
    <span class="task-card-id">T03</span>
    <span class="task-card-title">从历史会话中找到上次提到的某个文档</span>
  </div>
  <div class="task-card-stats">
    <span class="danger">完成率 <strong>38%</strong></span>
    <span>出错 <strong>2.3</strong></span>
    <span>满意度 <strong>4.2</strong></span>
  </div>
</div>
```

**严重等级标识**(左边框):
- 致命任务:`border-left: 3px solid var(--sev-fatal);`
- 严重任务:`border-left: 3px solid var(--sev-serious);`
- 正常任务:无左边框

**完成率染色**:< 50% 用 `--sev-fatal` 色文字,50-80% 用默认色。

## 7. 数据来源标注

每张图表下方必须标注数据来源:

```html
<div class="data-source">数据来源:整体满意度问卷 · n=12 · 10 点量表 · 取均值</div>
```

```css
.data-source {
  font-size: 11px;
  color: var(--text-3);
  font-family: var(--font-mono);
  margin-top: 8px;
  padding-top: 10px;
  border-top: 0.5px solid var(--line);
}
```

## 8. 不要使用的图表类型

为保持视觉简洁,以下图表**默认不使用**:

- 3D 饼图 / 3D 柱状图(过时)
- 折线图(报告中很少有时间序列数据)
- 散点图(除非用于"完成率 vs 满意度"任务对比)
- 词云(美观度差,且不易于打印)
- 地图(实现复杂,数据稀疏时不直观)

如果用户提供的数据**确实需要**这些图表,模型应在中间态卡片中标注"需要 XX 类型图表",由用户确认后再实现。
