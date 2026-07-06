# Interaction Patterns

报告中常用的交互行为实现。所有 JS 内联在 HTML 文件末尾,不引入第三方库。

## 1. 顶部锚点导航

**行为**:点击导航跳到对应章节,滚动时高亮当前章节。

```html
<nav class="topnav">
  <span class="brand">XXX 项目 · UX 评估报告</span>
  <div class="links">
    <a href="#cover">封面</a>
    <a href="#background">研究设计</a>
    <a href="#overview">结果总览</a>
    <a href="#problems">问题深挖</a>
    <a href="#appendix">附录</a>
  </div>
</nav>
```

```css
.topnav {
  position: sticky; top: 0;
  background: rgba(250,250,248,0.95);
  backdrop-filter: blur(8px);
  border-bottom: 0.5px solid var(--line);
  z-index: 100;
  padding: 12px 32px;
  display: flex; align-items: center; gap: 24px;
  font-size: 13px;
}
.topnav a {
  color: var(--text-3); text-decoration: none;
  padding: 4px 8px; border-radius: 4px;
  transition: all 0.15s;
}
.topnav a:hover { color: var(--text); background: var(--bg-alt); }
.topnav a.active { color: var(--text); background: var(--bg-alt); font-weight: 500; }

html { scroll-behavior: smooth; }
```

```javascript
// 滚动时高亮当前章节
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.topnav a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) current = section.getAttribute('id');
  });
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) link.classList.add('active');
  });
});
```

## 2. 任务卡 / 数字卡 hover & 点击

**行为**:悬停浮起 + 边框变色 + 出现箭头,点击触发操作。

```css
.task-card {
  cursor: pointer;
  transition: all 0.15s;
  position: relative;
}
.task-card:hover {
  border-color: var(--accent);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(45,74,107,0.08);
}
.task-detail-arrow {
  position: absolute;
  right: 14px; top: 14px;
  font-size: 12px; color: var(--text-3);
  transition: transform 0.2s;
}
.task-card:hover .task-detail-arrow { transform: translateX(2px); color: var(--accent); }
```

**点击行为**:

```html
<div class="task-card" onclick="document.getElementById('problem-P-001').scrollIntoView({behavior:'smooth'})">...</div>
```

或者跳转到锚点:`<a href="#problem-P-001">` 包裹卡片。

## 3. 问题切换 Tab

**行为**:点击 tab 切换显示对应问题内容(同屏切换或滚动到对应锚点)。

### 方式 A:滚动到对应锚点(推荐)

每个问题独立一屏,tab 点击后滚动到对应屏。

```html
<div class="problem-tabs">
  <button class="problem-tab danger active" onclick="goToProblem('P-001')">P-001</button>
  <button class="problem-tab danger" onclick="goToProblem('P-002')">P-002</button>
  <!-- ... -->
</div>

<script>
function goToProblem(id) {
  document.querySelectorAll('.problem-tab').forEach(t => t.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('problem-' + id).scrollIntoView({behavior: 'smooth'});
}
</script>
```

### 方式 B:同屏切换内容(适合问题不多 < 5 个)

所有问题数据存在 JS 对象中,点击 tab 更新内容区。

```javascript
const problems = {
  'P-001': {
    title: '历史会话搜索结果与用户预期不一致',
    severity: '致命',
    // ... 其他字段
  },
  // ...
};

function switchProblem(id) {
  const p = problems[id];
  document.getElementById('problem-title').textContent = p.title;
  // ... 更新其他元素
}
```

**默认采用方式 A**,因为锚点滚动可被浏览器记忆,用户分享 URL 时也可定位。

## 4. 附录表格筛选

**行为**:点击筛选按钮,隐藏不匹配的行。

```html
<div class="filter-bar">
  <span class="label-f">筛选</span>
  <button class="filter-btn active" onclick="filterTable('all', this)">全部</button>
  <button class="filter-btn" onclick="filterTable('fatal', this)">致命</button>
  <button class="filter-btn" onclick="filterTable('serious', this)">严重</button>
  <button class="filter-btn" onclick="filterTable('normal', this)">一般</button>
  <button class="filter-btn" onclick="filterTable('hint', this)">提示</button>
</div>

<table id="problem-table">
  <tbody>
    <tr data-severity="fatal">...</tr>
    <tr data-severity="serious">...</tr>
    <!-- ... -->
  </tbody>
</table>

<script>
function filterTable(severity, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('#problem-table tbody tr').forEach(row => {
    if (severity === 'all' || row.dataset.severity === severity) {
      row.classList.remove('hidden');
    } else {
      row.classList.add('hidden');
    }
  });
}
</script>
```

## 5. 数字卡点击展开详情(可选)

**行为**:点击数字卡,弹出底部抽屉或扩展显示更多信息。

简单实现用浏览器原生 `<details>` 或自定义抽屉。如果数据量小,可直接用 `alert` 或 `<details>`:

```html
<details class="persona-detail">
  <summary class="persona-num-card">
    <div class="label">熟练用户</div>
    <div class="num">7</div>
  </summary>
  <div class="detail-content">
    <p>P01(产品经理 · 5 年 · 每日多次)</p>
    <p>P02(设计师 · 3 年 · 每日)</p>
    <!-- ... -->
  </div>
</details>
```

如果交互需要更复杂(动画、面板),用自定义 JS。

## 6. 现场照片放大查看(可选)

```html
<img class="bg-photo-img" src="..." onclick="openLightbox(this.src)" />

<div id="lightbox" class="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" src="" />
</div>

<script>
function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').style.display = 'flex';
}
function closeLightbox() {
  document.getElementById('lightbox').style.display = 'none';
}
</script>
```

```css
.lightbox {
  display: none;
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.85);
  align-items: center; justify-content: center;
  z-index: 1000;
  cursor: zoom-out;
}
.lightbox img { max-width: 90vw; max-height: 90vh; }
```

## 7. 进度条首次填充动画

```css
.h-bar .fill { transition: width 0.6s ease-out; }
```

页面加载时使用 `IntersectionObserver` 在元素进入视口时触发动画(可选,简单实现可省略):

```javascript
const bars = document.querySelectorAll('.h-bar .fill');
bars.forEach(bar => {
  bar.dataset.width = bar.style.width;
  bar.style.width = '0';
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.width = entry.target.dataset.width;
      observer.unobserve(entry.target);
    }
  });
});
bars.forEach(bar => observer.observe(bar));
```

## 8. 不要做的交互

**避免**:

- 弹窗广告式的 modal
- 自动播放的轮播图
- 复杂的拖拽、排序交互(报告是阅读物,不是工具)
- 鼠标尾迹、视差滚动等炫技效果
- 强制全屏的"演示模式"

报告的交互应该是**辅助阅读**,不是抢戏。
