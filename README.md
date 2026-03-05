<!DOCTYPE html>

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>الوحدة الأولى – إنترنت الأشياء IoT</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=Tajawal:wght@300;400;500;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0f1e;
    --bg2: #0d1528;
    --card: #111827;
    --border: rgba(99,179,237,0.15);
    --accent1: #38bdf8;
    --accent2: #818cf8;
    --accent3: #34d399;
    --accent4: #fb923c;
    --accent5: #f472b6;
    --accent6: #facc15;
    --text: #e2e8f0;
    --muted: #94a3b8;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Cairo', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

/* Starfield */
body::before {
content: ‘’;
position: fixed;
inset: 0;
background-image:
radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,0.5) 0%, transparent 100%),
radial-gradient(1px 1px at 30% 60%, rgba(255,255,255,0.3) 0%, transparent 100%),
radial-gradient(1px 1px at 50% 10%, rgba(255,255,255,0.4) 0%, transparent 100%),
radial-gradient(1px 1px at 70% 80%, rgba(255,255,255,0.3) 0%, transparent 100%),
radial-gradient(1px 1px at 90% 40%, rgba(255,255,255,0.5) 0%, transparent 100%),
radial-gradient(1px 1px at 15% 90%, rgba(255,255,255,0.2) 0%, transparent 100%),
radial-gradient(1px 1px at 80% 15%, rgba(255,255,255,0.4) 0%, transparent 100%),
radial-gradient(2px 2px at 45% 50%, rgba(56,189,248,0.2) 0%, transparent 100%);
pointer-events: none;
z-index: 0;
}

header {
position: relative;
z-index: 10;
text-align: center;
padding: 60px 20px 40px;
background: linear-gradient(180deg, rgba(56,189,248,0.06) 0%, transparent 100%);
border-bottom: 1px solid var(–border);
}
.unit-badge {
display: inline-block;
background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(129,140,248,0.2));
border: 1px solid rgba(56,189,248,0.4);
border-radius: 50px;
padding: 6px 24px;
font-size: 13px;
color: var(–accent1);
letter-spacing: 2px;
margin-bottom: 20px;
font-weight: 600;
}
header h1 {
font-family: ‘Tajawal’, sans-serif;
font-size: clamp(28px, 5vw, 52px);
font-weight: 800;
background: linear-gradient(135deg, #fff 30%, var(–accent1) 70%, var(–accent2));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
margin-bottom: 12px;
line-height: 1.2;
}
header p { color: var(–muted); font-size: 15px; }

/* Nav tabs */
.nav-tabs {
position: sticky;
top: 0;
z-index: 100;
display: flex;
gap: 8px;
padding: 14px 20px;
background: rgba(10,15,30,0.95);
backdrop-filter: blur(20px);
border-bottom: 1px solid var(–border);
overflow-x: auto;
scrollbar-width: none;
justify-content: center;
flex-wrap: wrap;
}
.nav-tabs::-webkit-scrollbar { display: none; }
.nav-tab {
flex-shrink: 0;
padding: 8px 18px;
border-radius: 50px;
border: 1px solid var(–border);
background: transparent;
color: var(–muted);
font-family: ‘Cairo’, sans-serif;
font-size: 13px;
font-weight: 600;
cursor: pointer;
transition: all 0.25s;
white-space: nowrap;
}
.nav-tab:hover { color: var(–text); border-color: rgba(255,255,255,0.3); }
.nav-tab.active {
color: #000;
font-weight: 700;
}

/* Sections */
.section {
display: none;
animation: fadeIn 0.4s ease;
position: relative;
z-index: 1;
}
.section.active { display: block; }
@keyframes fadeIn { from { opacity:0; transform: translateY(12px); } to { opacity:1; transform: translateY(0); } }

/* ==============================
MIND MAP SECTION
============================== */
.mindmap-container {
padding: 40px 20px;
max-width: 1200px;
margin: 0 auto;
}
.mindmap-title {
text-align: center;
font-size: 22px;
font-weight: 700;
color: var(–accent1);
margin-bottom: 10px;
}
.mindmap-subtitle {
text-align: center;
color: var(–muted);
font-size: 13px;
margin-bottom: 40px;
}

/* Central node */
.mindmap-center {
display: flex;
justify-content: center;
margin-bottom: 50px;
}
.center-node {
background: linear-gradient(135deg, #1e3a5f, #1a1f4e);
border: 2px solid var(–accent1);
border-radius: 20px;
padding: 28px 48px;
text-align: center;
box-shadow: 0 0 60px rgba(56,189,248,0.25), 0 0 120px rgba(56,189,248,0.1);
position: relative;
}
.center-node::before {
content: ‘’;
position: absolute;
inset: -1px;
border-radius: 20px;
background: linear-gradient(135deg, var(–accent1), var(–accent2));
z-index: -1;
opacity: 0.5;
}
.center-node .icon { font-size: 40px; margin-bottom: 8px; }
.center-node h2 {
font-size: 26px;
font-weight: 900;
color: #fff;
margin-bottom: 4px;
}
.center-node p { color: var(–accent1); font-size: 13px; }

/* Branch grid */
.branches-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
gap: 24px;
}
.branch {
background: var(–card);
border-radius: 16px;
border: 1px solid var(–border);
overflow: hidden;
transition: transform 0.3s, box-shadow 0.3s;
cursor: pointer;
}
.branch:hover {
transform: translateY(-4px);
box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.branch-header {
padding: 18px 20px;
display: flex;
align-items: center;
gap: 14px;
}
.branch-icon {
width: 48px; height: 48px;
border-radius: 12px;
display: flex; align-items: center; justify-content: center;
font-size: 22px;
flex-shrink: 0;
}
.branch-title { font-size: 17px; font-weight: 700; color: #fff; }
.branch-subtitle { font-size: 12px; color: var(–muted); margin-top: 2px; }
.branch-body {
padding: 0 20px 20px;
display: none;
}
.branch.open .branch-body { display: block; }
.branch-toggle {
margin-right: auto;
width: 28px; height: 28px;
border-radius: 50%;
border: 1px solid var(–border);
background: transparent;
color: var(–muted);
cursor: pointer;
font-size: 16px;
display: flex; align-items: center; justify-content: center;
transition: all 0.2s;
flex-shrink: 0;
}
.branch.open .branch-toggle { transform: rotate(45deg); color: #fff; }

/* Sub-nodes */
.sub-node {
background: rgba(255,255,255,0.04);
border-radius: 10px;
padding: 12px 14px;
margin-bottom: 8px;
border-right: 3px solid transparent;
transition: background 0.2s;
}
.sub-node:hover { background: rgba(255,255,255,0.07); }
.sub-node-title {
font-size: 14px;
font-weight: 600;
margin-bottom: 6px;
}
.sub-node-items {
list-style: none;
display: flex;
flex-wrap: wrap;
gap: 6px;
margin-top: 8px;
}
.sub-node-items li {
background: rgba(255,255,255,0.07);
border-radius: 20px;
padding: 3px 12px;
font-size: 12px;
color: var(–muted);
}
.tag {
display: inline-block;
border-radius: 20px;
padding: 3px 12px;
font-size: 11px;
font-weight: 600;
margin: 2px;
}

/* ==============================
LESSONS SECTIONS
============================== */
.lesson-container {
max-width: 900px;
margin: 0 auto;
padding: 40px 20px;
}
.lesson-hero {
background: linear-gradient(135deg, var(–card), rgba(17,24,39,0.8));
border: 1px solid var(–border);
border-radius: 20px;
padding: 32px;
margin-bottom: 32px;
position: relative;
overflow: hidden;
}
.lesson-hero::before {
content: attr(data-icon);
position: absolute;
left: -10px;
top: -20px;
font-size: 120px;
opacity: 0.05;
pointer-events: none;
}
.lesson-number {
font-size: 11px;
font-weight: 700;
letter-spacing: 3px;
margin-bottom: 10px;
text-transform: uppercase;
}
.lesson-title {
font-family: ‘Tajawal’, sans-serif;
font-size: 28px;
font-weight: 800;
color: #fff;
margin-bottom: 10px;
line-height: 1.3;
}
.lesson-desc { color: var(–muted); font-size: 14px; line-height: 1.8; }

/* Concept cards */
.concepts-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
gap: 16px;
margin-bottom: 24px;
}
.concept-card {
background: var(–card);
border: 1px solid var(–border);
border-radius: 14px;
padding: 20px;
transition: transform 0.2s;
}
.concept-card:hover { transform: translateY(-3px); }
.concept-icon { font-size: 28px; margin-bottom: 10px; }
.concept-name {
font-size: 15px;
font-weight: 700;
color: #fff;
margin-bottom: 8px;
}
.concept-def {
font-size: 13px;
color: var(–muted);
line-height: 1.7;
}

/* Table */
.info-table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
font-size: 14px;
border-radius: 12px;
overflow: hidden;
}
.info-table th {
padding: 12px 16px;
text-align: right;
font-weight: 700;
font-size: 13px;
letter-spacing: 0.5px;
}
.info-table td {
padding: 11px 16px;
border-top: 1px solid rgba(255,255,255,0.05);
color: var(–muted);
vertical-align: top;
line-height: 1.7;
}
.info-table tr:hover td { background: rgba(255,255,255,0.03); }

/* Section heading */
.section-heading {
display: flex;
align-items: center;
gap: 12px;
margin: 28px 0 16px;
}
.section-heading::before {
content: ‘’;
flex: 1;
height: 1px;
background: linear-gradient(to right, transparent, var(–border));
}
.section-heading span {
font-size: 13px;
font-weight: 700;
color: var(–muted);
white-space: nowrap;
letter-spacing: 1px;
text-transform: uppercase;
}
.section-heading::after {
content: ‘’;
flex: 1;
height: 1px;
background: linear-gradient(to left, transparent, var(–border));
}

/* Pills / tags */
.pills {
display: flex;
flex-wrap: wrap;
gap: 8px;
margin: 12px 0;
}
.pill {
padding: 6px 16px;
border-radius: 50px;
font-size: 13px;
font-weight: 600;
border: 1px solid transparent;
}

/* Steps */
.steps {
display: flex;
flex-direction: column;
gap: 12px;
margin: 16px 0;
}
.step {
display: flex;
gap: 16px;
align-items: flex-start;
background: rgba(255,255,255,0.03);
border-radius: 12px;
padding: 14px;
}
.step-num {
width: 32px; height: 32px;
border-radius: 50%;
display: flex; align-items: center; justify-content: center;
font-size: 14px;
font-weight: 800;
flex-shrink: 0;
}
.step-content h4 { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.step-content p { font-size: 13px; color: var(–muted); line-height: 1.7; }

/* Architecture diagram */
.arch-diagram {
display: flex;
flex-direction: column;
gap: 4px;
margin: 20px 0;
position: relative;
}
.arch-layer {
border-radius: 12px;
padding: 16px 20px;
display: flex;
align-items: center;
gap: 16px;
position: relative;
}
.arch-layer-num {
width: 36px; height: 36px;
border-radius: 50%;
display: flex; align-items: center; justify-content: center;
font-weight: 800;
font-size: 15px;
flex-shrink: 0;
}
.arch-layer-content h3 { font-size: 15px; font-weight: 700; color: #fff; }
.arch-layer-content p { font-size: 12px; color: var(–muted); margin-top: 3px; }
.arch-arrow {
text-align: center;
font-size: 20px;
color: var(–muted);
line-height: 1;
}

/* Security cards */
.security-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
gap: 12px;
margin: 16px 0;
}
.sec-card {
background: rgba(255,255,255,0.04);
border-radius: 12px;
padding: 16px;
border: 1px solid var(–border);
text-align: center;
}
.sec-card .icon { font-size: 28px; margin-bottom: 8px; }
.sec-card h4 { font-size: 13px; font-weight: 700; color: #fff; margin-bottom: 6px; }
.sec-card p { font-size: 12px; color: var(–muted); line-height: 1.6; }

/* Scenarios */
.scenario-cards {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 16px;
margin: 16px 0;
}
.scenario-card {
border-radius: 14px;
padding: 20px;
border: 1px solid transparent;
position: relative;
overflow: hidden;
}
.scenario-num {
font-size: 48px;
font-weight: 900;
opacity: 0.15;
position: absolute;
top: 8px;
left: 16px;
line-height: 1;
font-family: ‘Tajawal’, sans-serif;
}
.scenario-card h3 { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
.scenario-card p { font-size: 13px; color: var(–muted); line-height: 1.7; }

/* Summary section */
.summary-section {
max-width: 900px;
margin: 0 auto;
padding: 40px 20px;
}
.summary-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
gap: 20px;
margin-bottom: 32px;
}
.summary-card {
background: var(–card);
border: 1px solid var(–border);
border-radius: 16px;
padding: 24px;
transition: transform 0.2s;
}
.summary-card:hover { transform: translateY(-4px); }
.summary-card h3 { font-size: 16px; font-weight: 700; margin-bottom: 14px; color: #fff; }
.summary-item {
display: flex;
align-items: flex-start;
gap: 10px;
margin-bottom: 10px;
font-size: 13px;
color: var(–muted);
line-height: 1.6;
}
.summary-item::before {
content: ‘◆’;
font-size: 8px;
margin-top: 5px;
flex-shrink: 0;
}

/* Responsive */
@media(max-width: 600px) {
.branches-grid { grid-template-columns: 1fr; }
.concepts-grid { grid-template-columns: 1fr; }
.scenario-cards { grid-template-columns: 1fr; }
}
</style>

</head>
<body>

<header>
  <div class="unit-badge">📡 الصف العاشر • الفصل الثاني</div>
  <h1>الوحدة الأولى: إنترنت الأشياء IoT</h1>
</header>

<nav class="nav-tabs">
  <button class="nav-tab active" onclick="showSection('mindmap')" id="tab-mindmap" style="background:#38bdf8;">🗺️ الخريطة الذهنية</button>
  <button class="nav-tab" onclick="showSection('l1')" id="tab-l1">الدرس ١: مقدمة IoT</button>
  <button class="nav-tab" onclick="showSection('l2')" id="tab-l2">الدرس ٢: البيت الذكي</button>
  <button class="nav-tab" onclick="showSection('l3')" id="tab-l3">الدرس ٣: الشبكات والبيانات</button>
  <button class="nav-tab" onclick="showSection('l5')" id="tab-l5">الدرس ٥: تطبيقات التصميم</button>
  <button class="nav-tab" onclick="showSection('summary')" id="tab-summary">📋 الملخص الكامل</button>
</nav>

<!-- ======================== MIND MAP ======================== -->

<div class="section active" id="section-mindmap">
  <div class="mindmap-container">
    <div class="mindmap-title">🧠 الخريطة الذهنية الشاملة</div>
    <div class="mindmap-subtitle">اضغط على أي فرع لتوسيعه والاطلاع على التفاصيل</div>

```
<div class="mindmap-center">
  <div class="center-node">
    <div class="icon">🌐</div>
    <h2>إنترنت الأشياء</h2>
    <p>Internet of Things – IoT</p>
  </div>
</div>

<div class="branches-grid">

  <!-- Branch 1 -->
  <div class="branch" id="b1" style="border-color: rgba(56,189,248,0.3);">
    <div class="branch-header" onclick="toggleBranch('b1')" style="background: linear-gradient(135deg, rgba(56,189,248,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(56,189,248,0.15); color: #38bdf8;">🔍</div>
      <div>
        <div class="branch-title">تعريف IoT ومكوناته</div>
        <div class="branch-subtitle">الدرس الأول</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #38bdf8;">
        <div class="sub-node-title" style="color:#38bdf8;">📌 التعريف</div>
        <p style="font-size:13px;color:var(--muted);line-height:1.7">شبكة من الأجهزة الإلكترونية المترابطة التي تجمع وتشارك البيانات عبر الإنترنت دون تدخل بشري مباشر</p>
      </div>
      <div class="sub-node" style="border-color: #38bdf8;">
        <div class="sub-node-title" style="color:#38bdf8;">📦 تصنيف الأشياء</div>
        <ul class="sub-node-items">
          <li>🏠 ثابتة: أجهزة المنزل الذكي</li>
          <li>📱 متنقلة: الساعات الذكية</li>
          <li>🚗 متنقلة: السيارات الذكية</li>
          <li>👓 متنقلة: Google Glass</li>
        </ul>
      </div>
      <div class="sub-node" style="border-color: #38bdf8;">
        <div class="sub-node-title" style="color:#38bdf8;">⚙️ مكونات النظام الرئيسية</div>
        <ul class="sub-node-items">
          <li>Sensors حساسات</li>
          <li>Actuators مشغلات</li>
          <li>MCU متحكم</li>
          <li>SBC حاسوب لوحي</li>
          <li>Cloud سحابة</li>
          <li>Gateway بوابة</li>
        </ul>
      </div>
      <div class="sub-node" style="border-color: #38bdf8;">
        <div class="sub-node-title" style="color:#38bdf8;">📡 بروتوكولات الاتصال</div>
        <ul class="sub-node-items">
          <li>📶 Wi-Fi</li>
          <li>🔵 Bluetooth</li>
          <li>🐝 Zigbee</li>
          <li>🌐 IoT Gateway</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Branch 2 -->
  <div class="branch" id="b2" style="border-color: rgba(52,211,153,0.3);">
    <div class="branch-header" onclick="toggleBranch('b2')" style="background: linear-gradient(135deg, rgba(52,211,153,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(52,211,153,0.15); color: #34d399;">🏠</div>
      <div>
        <div class="branch-title">المنزل الذكي</div>
        <div class="branch-subtitle">الدرس الثاني</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #34d399;">
        <div class="sub-node-title" style="color:#34d399;">📌 التعريف</div>
        <p style="font-size:13px;color:var(--muted);line-height:1.7">منزل مجهز بتقنيات حديثة تتيح للمستخدم التحكم في الأجهزة المنزلية عن بُعد عبر الهاتف الذكي أو الأوامر الصوتية</p>
      </div>
      <div class="sub-node" style="border-color: #34d399;">
        <div class="sub-node-title" style="color:#34d399;">🔧 أجهزة المنزل الذكي</div>
        <ul class="sub-node-items">
          <li>💡 الإضاءة الذكية</li>
          <li>❄️ المكيف الذكي</li>
          <li>🔒 قفل الباب الذكي</li>
          <li>🎙️ Alexa / Google Home</li>
          <li>📹 كاميرات الأمان</li>
          <li>🌡️ ميزان الحرارة</li>
          <li>🧊 الثلاجة الذكية</li>
          <li>🔥 كاشف الحريق</li>
        </ul>
      </div>
      <div class="sub-node" style="border-color: #34d399;">
        <div class="sub-node-title" style="color:#34d399;">⚡ آلية العمل</div>
        <ul class="sub-node-items">
          <li>🔗 طبقة الاتصال</li>
          <li>🎛️ التحكم المركزي</li>
          <li>🤖 التشغيل التلقائي</li>
          <li>📊 تحليل البيانات</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Branch 3 -->
  <div class="branch" id="b3" style="border-color: rgba(129,140,248,0.3);">
    <div class="branch-header" onclick="toggleBranch('b3')" style="background: linear-gradient(135deg, rgba(129,140,248,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(129,140,248,0.15); color: #818cf8;">🏗️</div>
      <div>
        <div class="branch-title">هيكلية شبكة IoT</div>
        <div class="branch-subtitle">الدرس الثالث</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #818cf8;">
        <div class="sub-node-title" style="color:#818cf8;">طبقة الإدراك (الأولى)</div>
        <p style="font-size:13px;color:var(--muted);line-height:1.7">وحدة الاستشعار + وحدة المعالجة + وحدة الذاكرة + وحدة الطاقة + المشغل</p>
      </div>
      <div class="sub-node" style="border-color: #818cf8;">
        <div class="sub-node-title" style="color:#818cf8;">طبقة الشبكة (الثانية)</div>
        <p style="font-size:13px;color:var(--muted);line-height:1.7">المعالجة المسبقة للبيانات + الحوسبة الضبابية (Fog) + نقل البيانات عبر الشبكة</p>
      </div>
      <div class="sub-node" style="border-color: #818cf8;">
        <div class="sub-node-title" style="color:#818cf8;">طبقة التطبيق (الثالثة)</div>
        <p style="font-size:13px;color:var(--muted);line-height:1.7">تخزين البيانات + معالجة متقدمة + عرض واجهة المستخدم</p>
      </div>
    </div>
  </div>

  <!-- Branch 4 -->
  <div class="branch" id="b4" style="border-color: rgba(251,146,60,0.3);">
    <div class="branch-header" onclick="toggleBranch('b4')" style="background: linear-gradient(135deg, rgba(251,146,60,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(251,146,60,0.15); color: #fb923c;">💾</div>
      <div>
        <div class="branch-title">جمع البيانات</div>
        <div class="branch-subtitle">الدرس الثالث</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #fb923c;">
        <div class="sub-node-title" style="color:#fb923c;">المرحلة ١: توليد البيانات</div>
        <p style="font-size:13px;color:var(--muted)">تجمع أجهزة الاستشعار البيانات المتعلقة بتغيرات البيئة المحيطة</p>
      </div>
      <div class="sub-node" style="border-color: #fb923c;">
        <div class="sub-node-title" style="color:#fb923c;">المرحلة ٢: نقل البيانات</div>
        <p style="font-size:13px;color:var(--muted)">تُنقل البيانات عبر بوابات IoT إلى نظام مركزي أو سحابي</p>
      </div>
      <div class="sub-node" style="border-color: #fb923c;">
        <div class="sub-node-title" style="color:#fb923c;">المرحلة ٣: تخزين واسترجاع</div>
        <p style="font-size:13px;color:var(--muted)">تُخزن البيانات في قواعد بيانات يمكن الوصول إليها في أي وقت</p>
      </div>
      <div class="sub-node" style="border-color: #fb923c;">
        <div class="sub-node-title" style="color:#fb923c;">🛰️ نظام GPS</div>
        <p style="font-size:13px;color:var(--muted)">يعتمد على أكثر من 30 قمرًا صناعيًا لتحديد الموقع بدقة عالية</p>
      </div>
    </div>
  </div>

  <!-- Branch 5 -->
  <div class="branch" id="b5" style="border-color: rgba(244,114,182,0.3);">
    <div class="branch-header" onclick="toggleBranch('b5')" style="background: linear-gradient(135deg, rgba(244,114,182,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(244,114,182,0.15); color: #f472b6;">🔐</div>
      <div>
        <div class="branch-title">أمن IoT</div>
        <div class="branch-subtitle">الدرس الثالث</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #f472b6;">
        <div class="sub-node-title" style="color:#f472b6;">⚠️ التهديدات</div>
        <ul class="sub-node-items">
          <li>هجمات التسلل</li>
          <li>التصيد الاحتيالي</li>
          <li>كلمات مرور ضعيفة</li>
          <li>غياب التشفير</li>
          <li>القيود على الموارد</li>
        </ul>
      </div>
      <div class="sub-node" style="border-color: #f472b6;">
        <div class="sub-node-title" style="color:#f472b6;">✅ إجراءات الحماية</div>
        <ul class="sub-node-items">
          <li>تحديث الأجهزة والبرامج</li>
          <li>تغيير كلمات المرور دوريًا</li>
          <li>استخدام التشفير</li>
          <li>الاستخدام المسؤول</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Branch 6 -->
  <div class="branch" id="b6" style="border-color: rgba(250,204,21,0.3);">
    <div class="branch-header" onclick="toggleBranch('b6')" style="background: linear-gradient(135deg, rgba(250,204,21,0.12), transparent);">
      <div class="branch-icon" style="background: rgba(250,204,21,0.15); color: #facc15;">🛠️</div>
      <div>
        <div class="branch-title">تصميم شبكات IoT</div>
        <div class="branch-subtitle">الدرس الخامس</div>
      </div>
      <button class="branch-toggle">+</button>
    </div>
    <div class="branch-body">
      <div class="sub-node" style="border-color: #facc15;">
        <div class="sub-node-title" style="color:#facc15;">🖥️ برنامج Packet Tracer</div>
        <p style="font-size:13px;color:var(--muted)">برنامج محاكاة شبكات من Cisco يُستخدم لتصميم وتطبيق سيناريوهات IoT</p>
      </div>
      <div class="sub-node" style="border-color: #facc15;">
        <div class="sub-node-title" style="color:#facc15;">📋 خطوات التصميم</div>
        <ul class="sub-node-items">
          <li>١. تحديد المشكلة</li>
          <li>٢. تحليل الاحتياجات</li>
          <li>٣. اختيار المكونات</li>
          <li>٤. تصميم الشبكة</li>
          <li>٥. الاختبار والتحقق</li>
        </ul>
      </div>
      <div class="sub-node" style="border-color: #facc15;">
        <div class="sub-node-title" style="color:#facc15;">🏠 سيناريوهات التطبيق</div>
        <ul class="sub-node-items">
          <li>التحكم عبر Home Gateway</li>
          <li>التحكم عبر Server + AP</li>
          <li>نظام إطفاء الحريق</li>
          <li>موقف السيارات الذكي</li>
        </ul>
      </div>
    </div>
  </div>

</div>
```

  </div>
</div>

<!-- ======================== LESSON 1 ======================== -->

<div class="section" id="section-l1">
  <div class="lesson-container">
    <div class="lesson-hero" data-icon="🔍" style="border-color: rgba(56,189,248,0.3);">
      <div class="lesson-number" style="color:#38bdf8;">الدرس الأول</div>
      <div class="lesson-title">مقدمة إنترنت الأشياء – IoT</div>
      <div class="lesson-desc">شبكة من الأجهزة الإلكترونية المترابطة التي تجمع وتشارك البيانات عبر الإنترنت دون تدخل بشري مباشر، تضم حساسات وبرمجيات وتقنيات اتصال.</div>
    </div>

```
<div class="section-heading"><span>تصنيف الأشياء</span></div>
<div class="concepts-grid">
  <div class="concept-card" style="border-color: rgba(56,189,248,0.3);">
    <div class="concept-icon">🏠</div>
    <div class="concept-name">أشياء ثابتة (Fixed)</div>
    <div class="concept-def">الأجهزة المنزلية كالأفران والثلاجات والمكيفات المرتبطة بشبكة الإنترنت في مكان ثابت</div>
  </div>
  <div class="concept-card" style="border-color: rgba(52,211,153,0.3);">
    <div class="concept-icon">📱</div>
    <div class="concept-name">أشياء متنقلة (Mobile)</div>
    <div class="concept-def">الهواتف الذكية، الساعات الذكية، Google Glass، السيارات الذكية – تتحرك مع المستخدم</div>
  </div>
</div>

<div class="section-heading"><span>مكونات نظام IoT</span></div>
<table class="info-table">
  <thead><tr style="background: rgba(56,189,248,0.15);">
    <th style="color:#38bdf8;">المكوّن</th>
    <th style="color:#38bdf8;">الوظيفة</th>
    <th style="color:#38bdf8;">مثال</th>
  </tr></thead>
  <tbody>
    <tr><td>🔬 الحساسات (Sensors)</td><td>قراءة البيانات من البيئة المحيطة</td><td>حساس الحرارة، حساس الحركة</td></tr>
    <tr><td>⚙️ المشغلات (Actuators)</td><td>تنفيذ الأوامر وإحداث تأثير مادي</td><td>محرك، صمام، مصباح</td></tr>
    <tr><td>🖥️ أجهزة IoT</td><td>المعالجة والتحكم</td><td>MCU ميكروكنترولر، SBC حاسوب لوحي</td></tr>
    <tr><td>📡 وسيط الاتصال</td><td>نقل البيانات بين الأجهزة</td><td>Wi-Fi, Bluetooth, Zigbee</td></tr>
    <tr><td>☁️ منصة السحابة</td><td>تخزين ومعالجة البيانات</td><td>AWS, Google Cloud, Azure</td></tr>
    <tr><td>📲 واجهة المستخدم</td><td>التحكم وعرض المعلومات</td><td>تطبيق الهاتف، لوحة التحكم</td></tr>
  </tbody>
</table>

<div class="section-heading"><span>أجهزة IoT: MCU vs SBC</span></div>
<div class="concepts-grid">
  <div class="concept-card" style="border-color: rgba(56,189,248,0.3);">
    <div class="concept-icon">🔲</div>
    <div class="concept-name">الميكروكنترولر (MCU)</div>
    <div class="concept-def">حاسوب صغير مدمج مخصص لأداء مهام محددة وبسيطة. يعمل بشكل خفي داخل أجهزة IoT. مثل: Arduino</div>
  </div>
  <div class="concept-card" style="border-color: rgba(52,211,153,0.3);">
    <div class="concept-icon">🖥️</div>
    <div class="concept-name">الحاسوب اللوحي (SBC)</div>
    <div class="concept-def">حاسوب كامل على لوحة واحدة بقدرات أعلى من MCU. يدعم أنظمة تشغيل كاملة. مثل: Raspberry Pi</div>
  </div>
</div>

<div class="section-heading"><span>بروتوكولات الاتصال</span></div>
<div class="concepts-grid">
  <div class="concept-card" style="border-color: rgba(56,189,248,0.2);">
    <div class="concept-icon">📶</div>
    <div class="concept-name">Wi-Fi</div>
    <div class="concept-def">للاتصال بالشبكة المحلية والإنترنت. مدى متوسط، سرعة عالية. الأنسب للبيئات المنزلية.</div>
  </div>
  <div class="concept-card" style="border-color: rgba(96,165,250,0.2);">
    <div class="concept-icon">🔵</div>
    <div class="concept-name">Bluetooth</div>
    <div class="concept-def">للاتصال القريب بين الأجهزة. مدى قصير، استهلاك طاقة منخفض. مناسب للأجهزة القابلة للارتداء.</div>
  </div>
  <div class="concept-card" style="border-color: rgba(250,204,21,0.2);">
    <div class="concept-icon">🐝</div>
    <div class="concept-name">Zigbee</div>
    <div class="concept-def">بروتوكول لاسلكي منخفض الطاقة. يُستخدم في المدن الذكية والزراعة الذكية. يدعم شبكات كبيرة من الأجهزة.</div>
  </div>
  <div class="concept-card" style="border-color: rgba(52,211,153,0.2);">
    <div class="concept-icon">🌐</div>
    <div class="concept-name">IoT Gateway بوابة</div>
    <div class="concept-def">تربط الشبكة اللاسلكية بالمستوى الرقمي السحابي. تجمع البيانات وترسلها للمعالجة.</div>
  </div>
</div>
```

  </div>
</div>

<!-- ======================== LESSON 2 ======================== -->

<div class="section" id="section-l2">
  <div class="lesson-container">
    <div class="lesson-hero" data-icon="🏠" style="border-color: rgba(52,211,153,0.3);">
      <div class="lesson-number" style="color:#34d399;">الدرس الثاني</div>
      <div class="lesson-title">أمثلة عملية على الأنظمة الذكية</div>
      <div class="lesson-desc">المنزل الذكي هو منزل مجهز بتقنيات حديثة تتيح للمستخدم التحكم في الأجهزة المنزلية عن بُعد، مما يعزز الراحة والأمان ويوفر في استهلاك الطاقة.</div>
    </div>

```
<div class="section-heading"><span>أبرز أجهزة المنزل الذكي</span></div>
<div class="concepts-grid">
  <div class="concept-card" style="border-color:rgba(250,204,21,0.2)">
    <div class="concept-icon">⏰</div>
    <div class="concept-name">المنبّه الذكي (Smart Time Clock)</div>
    <div class="concept-def">يجمع بيانات النوم ويضبط الإيقاظ في الوقت الأنسب حسب دورة النوم</div>
  </div>
  <div class="concept-card" style="border-color:rgba(244,114,182,0.2)">
    <div class="concept-icon">📹</div>
    <div class="concept-name">كاميرات المراقبة الذكية</div>
    <div class="concept-def">تراقب داخل وخارج المنزل، تكشف الحركة، وتتعرف على الوجوه. تُرسل تنبيهات فورية.</div>
  </div>
  <div class="concept-card" style="border-color:rgba(251,146,60,0.2)">
    <div class="concept-icon">🌡️</div>
    <div class="concept-name">ميزان الحرارة الذكي</div>
    <div class="concept-def">يضبط درجة الحرارة تلقائيًا حسب جدول زمني مسبق أو الاحتياجات الحالية</div>
  </div>
  <div class="concept-card" style="border-color:rgba(56,189,248,0.2)">
    <div class="concept-icon">💡</div>
    <div class="concept-name">المصابيح الذكية</div>
    <div class="concept-def">تغيير لون الإضاءة والتحكم في شدتها عن بُعد عبر تطبيق الهاتف</div>
  </div>
  <div class="concept-card" style="border-color:rgba(52,211,153,0.2)">
    <div class="concept-icon">🔒</div>
    <div class="concept-name">قفل الباب الذكي</div>
    <div class="concept-def">يفتح ويغلق عبر الهاتف أو بصمة الإصبع، ويتيح منح إذن الدخول للضيوف عن بُعد</div>
  </div>
  <div class="concept-card" style="border-color:rgba(129,140,248,0.2)">
    <div class="concept-icon">🎙️</div>
    <div class="concept-name">المساعدات الصوتية الذكية</div>
    <div class="concept-def">تتحكم في جميع أجهزة المنزل بالأوامر الصوتية. مثل: Amazon Alexa، Google Home</div>
  </div>
  <div class="concept-card" style="border-color:rgba(244,114,182,0.2)">
    <div class="concept-icon">🧊</div>
    <div class="concept-name">الثلاجة الذكية</div>
    <div class="concept-def">تعرض وصفات الطبخ، تدير قائمة التسوق، وتراقب صلاحية المنتجات داخلها</div>
  </div>
  <div class="concept-card" style="border-color:rgba(251,146,60,0.2)">
    <div class="concept-icon">🔥</div>
    <div class="concept-name">نظام إنذار الحريق الذكي</div>
    <div class="concept-def">يكتشف الدخان والحرارة ويُطلق صفارات الإنذار ويُشغل نظام الرش تلقائيًا</div>
  </div>
</div>

<div class="section-heading"><span>آلية عمل المنازل الذكية</span></div>
<div class="steps">
  <div class="step">
    <div class="step-num" style="background:rgba(52,211,153,0.2);color:#34d399;">١</div>
    <div class="step-content">
      <h4>الاتصال بالشبكة</h4>
      <p>تعتمد الأجهزة الذكية على تطبيقات مخصصة في الهاتف الذكي أو الحاسوب للاتصال بالشبكة المحلية أو الإنترنت</p>
    </div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(52,211,153,0.2);color:#34d399;">٢</div>
    <div class="step-content">
      <h4>التشغيل التلقائي</h4>
      <p>يمكن للمنازل الذكية العمل بصورة تلقائية وفق لظروف معينة يحددها المستخدم كتشغيل المكيف عند الاقتراب</p>
    </div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(52,211,153,0.2);color:#34d399;">٣</div>
    <div class="step-content">
      <h4>التكامل بين الأجهزة</h4>
      <p>تتكامل الأجهزة الذكية فيما بينها لتنسيق تحسين الأداء، كدمج كاميرا الأمان مع جرس الباب لتكوين نظام حماية متكامل</p>
    </div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(52,211,153,0.2);color:#34d399;">٤</div>
    <div class="step-content">
      <h4>معالجة البيانات والتعلم</h4>
      <p>تجمع أنظمة المنازل الذكية بيانات من أجهزة الاستشعار لفهم عادات المستخدم، وتوظفها في ترشيد استهلاك الطاقة وتعزيز الأمان</p>
    </div>
  </div>
</div>

<div class="section-heading"><span>أنظمة أخرى تحتوي حساسًا ومشغلًا</span></div>
<div class="pills">
  <span class="pill" style="background:rgba(52,211,153,0.1);border-color:rgba(52,211,153,0.3);color:#34d399;">🔥 نظام إنذار الحريق الذكي</span>
  <span class="pill" style="background:rgba(56,189,248,0.1);border-color:rgba(56,189,248,0.3);color:#38bdf8;">🚦 إشارات المرور الذكية</span>
  <span class="pill" style="background:rgba(251,146,60,0.1);border-color:rgba(251,146,60,0.3);color:#fb923c;">🚗 أنظمة فتح أبواب السيارات</span>
  <span class="pill" style="background:rgba(129,140,248,0.1);border-color:rgba(129,140,248,0.3);color:#818cf8;">💧 أنظمة الري الذكي</span>
  <span class="pill" style="background:rgba(244,114,182,0.1);border-color:rgba(244,114,182,0.3);color:#f472b6;">💓 أجهزة مراقبة ضربات القلب</span>
</div>
```

  </div>
</div>

<!-- ======================== LESSON 3 ======================== -->

<div class="section" id="section-l3">
  <div class="lesson-container">
    <div class="lesson-hero" data-icon="🌐" style="border-color: rgba(129,140,248,0.3);">
      <div class="lesson-number" style="color:#818cf8;">الدرس الثالث</div>
      <div class="lesson-title">تصميم الشبكات وجمع البيانات</div>
      <div class="lesson-desc">يشرح هذا الدرس كيفية عمل نظام IoT وكيف تتواصل مكوناته، مع شرح هيكلية الشبكة بثلاث طبقات، ومراحل جمع البيانات، وأمثلة تطبيقية.</div>
    </div>

```
<div class="section-heading"><span>سيناريوهات التواصل في IoT</span></div>
<div class="scenario-cards">
  <div class="scenario-card" style="background:rgba(56,189,248,0.07);border-color:rgba(56,189,248,0.2);">
    <div class="scenario-num" style="color:#38bdf8;">١</div>
    <h3 style="color:#38bdf8;">الجهاز إلى السحابة</h3>
    <p>يُرسل جهاز IoT بياناته إلى السحابة للتحليل وتحسين الأداء، مثل رصد حركة الزوار في معرض فني</p>
  </div>
  <div class="scenario-card" style="background:rgba(52,211,153,0.07);border-color:rgba(52,211,153,0.2);">
    <div class="scenario-num" style="color:#34d399;">٢</div>
    <h3 style="color:#34d399;">تحليل في الوقت الفعلي</h3>
    <p>تُحلل البيانات من أجهزة IoT فوريًا وترسل النتائج للجهاز لمساعدته على اتخاذ قرارات أفضل</p>
  </div>
  <div class="scenario-card" style="background:rgba(251,146,60,0.07);border-color:rgba(251,146,60,0.2);">
    <div class="scenario-num" style="color:#fb923c;">٣</div>
    <h3 style="color:#fb923c;">الجهاز إلى جهاز</h3>
    <p>يُرسل الجهاز بياناته للسحابة ثم ترسل السحابة أوامر لجهاز آخر، كجهاز تتبع النوم الذي يُشغل القهوة صباحًا</p>
  </div>
</div>

<div class="section-heading"><span>هيكلية شبكة IoT (ثلاث طبقات)</span></div>
<div class="arch-diagram">
  <div class="arch-layer" style="background:rgba(251,146,60,0.1);border:1px solid rgba(251,146,60,0.3);">
    <div class="arch-layer-num" style="background:rgba(251,146,60,0.2);color:#fb923c;">٣</div>
    <div class="arch-layer-content">
      <h3 style="color:#fb923c;">طبقة التطبيق (Application Layer)</h3>
      <p>تخزين البيانات + معالجة متقدمة + عرض واجهة المستخدم النهائي | السحابة / الخوادم</p>
    </div>
  </div>
  <div class="arch-arrow">⬇️</div>
  <div class="arch-layer" style="background:rgba(129,140,248,0.1);border:1px solid rgba(129,140,248,0.3);">
    <div class="arch-layer-num" style="background:rgba(129,140,248,0.2);color:#818cf8;">٢</div>
    <div class="arch-layer-content">
      <h3 style="color:#818cf8;">طبقة الشبكة (Network Layer)</h3>
      <p>المعالجة المسبقة (Preprocessing) + الحوسبة الضبابية Fog/Edge + نقل البيانات | أجهزة التوجيه والبوابات</p>
    </div>
  </div>
  <div class="arch-arrow">⬇️</div>
  <div class="arch-layer" style="background:rgba(56,189,248,0.1);border:1px solid rgba(56,189,248,0.3);">
    <div class="arch-layer-num" style="background:rgba(56,189,248,0.2);color:#38bdf8;">١</div>
    <div class="arch-layer-content">
      <h3 style="color:#38bdf8;">طبقة الإدراك (Perception Layer)</h3>
      <p>أجهزة الاستشعار + المشغلات + جمع البيانات من العالم الفيزيائي</p>
    </div>
  </div>
</div>

<div class="section-heading"><span>مكونات طبقة الإدراك بالتفصيل</span></div>
<table class="info-table">
  <thead><tr style="background:rgba(56,189,248,0.15);">
    <th style="color:#38bdf8;">الوحدة</th><th style="color:#38bdf8;">الوظيفة</th>
  </tr></thead>
  <tbody>
    <tr><td>🔬 وحدة الاستشعار (Sensor Unit)</td><td>تتفاعل مع العالم الخارجي وتجمع البيانات الفيزيائية وتحوّلها إلى إشارات رقمية</td></tr>
    <tr><td>⚡ وحدة المعالجة (Processing Unit)</td><td>تؤدي المهام وتعالج البيانات وتتحكم في المكونات الأخرى</td></tr>
    <tr><td>💾 وحدة الذاكرة (Memory Unit)</td><td>تحفظ بعض البيانات التي عولجت مؤقتًا</td></tr>
    <tr><td>📡 وحدة الإرسال والاستقبال</td><td>تربط جهاز الاستشعار بالمكونات الأخرى لإرسال واستقبال البيانات</td></tr>
    <tr><td>🔋 وحدة الطاقة (Power Unit)</td><td>تزوّد الجهاز بالطاقة الكهربائية اللازمة للتشغيل</td></tr>
    <tr><td>⚙️ المشغّل (Actuator)</td><td>يستقبل إشارات التحكم وينفذها لإحداث تأثير مادي في البيئة</td></tr>
  </tbody>
</table>

<div class="section-heading"><span>مراحل جمع البيانات</span></div>
<div class="steps">
  <div class="step">
    <div class="step-num" style="background:rgba(56,189,248,0.2);color:#38bdf8;">١</div>
    <div class="step-content">
      <h4>توليد البيانات (Data Generation)</h4>
      <p>تعمل أجهزة الاستشعار على توليد البيانات المتعلقة بتغيرات البيئة المحيطة</p>
    </div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(129,140,248,0.2);color:#818cf8;">٢</div>
    <div class="step-content">
      <h4>نقل البيانات (Data Transmission)</h4>
      <p>تُنقل البيانات بعد توليدها إلى نظام مركزي أو سحابي. تستخدم بوابات IoT لتصفية البيانات وتأمينها قبل الإرسال</p>
    </div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(251,146,60,0.2);color:#fb923c;">٣</div>
    <div class="step-content">
      <h4>تخزين واسترجاع البيانات (Storage & Retrieval)</h4>
      <p>تُخزن البيانات في قواعد بيانات يمكن الوصول إليها في أي وقت للتحليل. تستخدم خوادم محلية أو منصات سحابية</p>
    </div>
  </div>
</div>

<div class="section-heading"><span>نظام تحديد المواقع GPS</span></div>
<div class="concept-card" style="border-color:rgba(250,204,21,0.3);margin-bottom:16px">
  <div class="concept-icon">🛰️</div>
  <div class="concept-name">كيف يعمل نظام GPS؟</div>
  <div class="concept-def">
    يعتمد على شبكة أكثر من 30 قمرًا صناعيًا تدور حول الأرض، تُرسل إشارات دقيقة ومتزامنة. جهاز الاستقبال يلتقي إشارات من 3 أو 4 أقمار ليحسب المسافة بينه وبين كل قمر، ثم يُحدد الموقع بدقة.
    <br><br>مكونات نظام GPS: الأقمار الصناعية + الأجهزة المستقبِلة + البرمجيات التي تعالج الإشارات وتحسب الموقع.
  </div>
</div>

<div class="section-heading"><span>أمن إنترنت الأشياء (IoT Security)</span></div>
<div class="security-grid">
  <div class="sec-card">
    <div class="icon">⚠️</div>
    <h4>هجمات التسلل</h4>
    <p>اختراق الأجهزة عبر الثغرات في البرامج أو الشبكات</p>
  </div>
  <div class="sec-card">
    <div class="icon">🎣</div>
    <h4>التصيد الاحتيالي</h4>
    <p>خداع المستخدم للحصول على بياناته الشخصية</p>
  </div>
  <div class="sec-card">
    <div class="icon">🔑</div>
    <h4>كلمات مرور ضعيفة</h4>
    <p>استخدام كلمات مرور يسهل تخمينها أو الافتراضية</p>
  </div>
  <div class="sec-card">
    <div class="icon">🔓</div>
    <h4>غياب التشفير</h4>
    <p>إرسال البيانات دون تشفير يعرضها للسرقة</p>
  </div>
</div>
<div class="section-heading"><span>✅ إجراءات الحماية الواجبة</span></div>
<div class="steps">
  <div class="step">
    <div class="step-num" style="background:rgba(244,114,182,0.2);color:#f472b6;">١</div>
    <div class="step-content"><h4>تحديث الأجهزة والبرامج</h4><p>متابعة تحديث البرمجيات والأجهزة في نظام IoT لضمان حمايتها باستمرار</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(244,114,182,0.2);color:#f472b6;">٢</div>
    <div class="step-content"><h4>تغيير كلمات المرور الافتراضية</h4><p>استخدام كلمات مرور قوية وتغييرها بصورة دورية لمنع الاختراقات</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(244,114,182,0.2);color:#f472b6;">٣</div>
    <div class="step-content"><h4>استخدام طرق التشفير</h4><p>استخدام طرق التشفير المختلفة في إعدادات أجهزة التوجيه ونقل البيانات</p></div>
  </div>
</div>
```

  </div>
</div>

<!-- ======================== LESSON 5 ======================== -->

<div class="section" id="section-l5">
  <div class="lesson-container">
    <div class="lesson-hero" data-icon="🛠️" style="border-color: rgba(250,204,21,0.3);">
      <div class="lesson-number" style="color:#facc15;">الدرس الخامس</div>
      <div class="lesson-title">تطبيقات عملية لتصميم شبكة IoT</div>
      <div class="lesson-desc">تطبيق عملي على سيناريوهات IoT باستخدام برنامج Cisco Packet Tracer، وتصميم شبكات IoT عملية تؤدي مهمة أو أكثر.</div>
    </div>

```
<div class="section-heading"><span>برنامج Packet Tracer</span></div>
<div class="concept-card" style="border-color:rgba(250,204,21,0.3);margin-bottom:20px;">
  <div class="concept-icon">🖥️</div>
  <div class="concept-name">ما هو Packet Tracer؟</div>
  <div class="concept-def">برنامج محاكاة شبكات من شركة Cisco يُستخدم لتصميم شبكات IoT ومحاكاتها في بيئة افتراضية آمنة قبل التطبيق الفعلي. يُعدّ من أنسب البرامج لمحاكاة شبكات IoT في سيناريوهات متعددة.</div>
</div>

<div class="section-heading"><span>مكونات شبكة IoT المتكاملة</span></div>
<table class="info-table">
  <thead><tr style="background:rgba(250,204,21,0.15);">
    <th style="color:#facc15;">المكوّن</th><th style="color:#facc15;">الدور</th>
  </tr></thead>
  <tbody>
    <tr><td>🏠 Home Gateway البوابة المنزلية</td><td>تربط جميع أجهزة المنزل الذكي بالشبكة وتتيح التحكم فيها</td></tr>
    <tr><td>🖥️ Server مخدم</td><td>يخزن البيانات ويدير أجهزة IoT ويتحكم في التشغيل التلقائي</td></tr>
    <tr><td>📶 Access Point نقطة وصول</td><td>تتيح الاتصال اللاسلكي للأجهزة بالشبكة</td></tr>
    <tr><td>🔀 Switch لوّحم</td><td>يوزع الاتصالات بين الأجهزة المتصلة بالكابل</td></tr>
    <tr><td>📱 End Devices الأجهزة الطرفية</td><td>الأجهزة النهائية: كاميرا، باب، نافذة، مروحة</td></tr>
    <tr><td>📋 SSID</td><td>اسم الشبكة اللاسلكية المُعرِّف لها</td></tr>
    <tr><td>⚙️ DHCP</td><td>بروتوكول يخصص عناوين IP تلقائيًا للأجهزة</td></tr>
  </tbody>
</table>

<div class="section-heading"><span>السيناريوهات التطبيقية الثلاثة</span></div>

<div style="margin-bottom: 16px;">
  <div class="scenario-card" style="background:rgba(56,189,248,0.07);border-color:rgba(56,189,248,0.25);margin-bottom:12px;">
    <div class="scenario-num" style="color:#38bdf8;">١</div>
    <h3 style="color:#38bdf8;">التحكم عبر البوابة المنزلية (Home Gateway)</h3>
    <p>شبكة تتكون من: بوابة منزلية + 4 أجهزة (باب، جراج، مروحة، إضاءة) + هاتف ذكي واحد. الاتصال عبر كابل FastEthernet أو لاسلكي عبر SSID البوابة.</p>
  </div>
  <div class="scenario-card" style="background:rgba(52,211,153,0.07);border-color:rgba(52,211,153,0.25);margin-bottom:12px;">
    <div class="scenario-num" style="color:#34d399;">٢</div>
    <h3 style="color:#34d399;">التحكم عبر المخدم ونقطة الوصول (Server + AP)</h3>
    <p>شبكة داخلية تتكون من: مخدم + لوّحم Switch + نقطة وصول + أجهزة متنوعة (باب، كاميرا، نافذة، مروحة) + حاسوب. تُضاف مستخدمون وتضبط شروط التشغيل التلقائي.</p>
  </div>
  <div class="scenario-card" style="background:rgba(251,146,60,0.07);border-color:rgba(251,146,60,0.25);">
    <div class="scenario-num" style="color:#fb923c;">٣</div>
    <h3 style="color:#fb923c;">نظام إطفاء الحريق الذكي</h3>
    <p>يضم: صفارة إنذار + كاشف دخان + نافذة + موقف سيارات + مروحة + رشاش حريق + سيارة + هاتف ذكي. تُضبط شروط ثلاثة حسب مستوى الدخان لتشغيل الأجهزة تدريجيًا.</p>
  </div>
</div>

<div class="section-heading"><span>خطوات تصميم مشروع IoT</span></div>
<div class="steps">
  <div class="step">
    <div class="step-num" style="background:rgba(250,204,21,0.2);color:#facc15;">١</div>
    <div class="step-content"><h4>تحديد المشكلة</h4><p>وصف المشكلة التي نسعى إلى حلها أو احتوائها باستخدام تقنية إنترنت الأشياء</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(250,204,21,0.2);color:#facc15;">٢</div>
    <div class="step-content"><h4>تحديد الحلول والجهات المستفيدة</h4><p>تحديد الحلول التي سننفذها باستخدام أجهزة IoT وتحديد الفئة المستهدفة (الطلاب، المعلمون، الإداريون)</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(250,204,21,0.2);color:#facc15;">٣</div>
    <div class="step-content"><h4>تحديد الأجهزة المطلوبة</h4><p>تحديد أجهزة IoT اللازمة لتنفيذ المشروع وتحقيق أهدافه</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(250,204,21,0.2);color:#facc15;">٤</div>
    <div class="step-content"><h4>إدراج النموذج المصمَّم</h4><p>تضمين النموذج الذي يُبيّن مكونات IoT المستخدمة لتحقيق أهداف المشروع</p></div>
  </div>
  <div class="step">
    <div class="step-num" style="background:rgba(250,204,21,0.2);color:#facc15;">٥</div>
    <div class="step-content"><h4>إنتاج الكتيّب التعريفي</h4><p>إعداد كتيّب (بروشور) إلكتروني باستخدام Canva أو PowerPoint يوضح آلية عمل المشروع وخطوات تنفيذه</p></div>
  </div>
</div>
```

  </div>
</div>

<!-- ======================== SUMMARY ======================== -->

<div class="section" id="section-summary">
  <div class="summary-section">
    <div class="mindmap-title">📋 الملخص الشامل للوحدة</div>
    <div class="mindmap-subtitle" style="margin-bottom:32px;">كل ما تحتاج معرفته من الوحدة الأولى في مكان واحد</div>

```
<div class="summary-grid">
  <div class="summary-card" style="border-color:rgba(56,189,248,0.3);">
    <h3 style="color:#38bdf8;">🌐 تعريف IoT</h3>
    <div class="summary-item">شبكة من الأجهزة الإلكترونية المترابطة تجمع وتشارك البيانات عبر الإنترنت</div>
    <div class="summary-item">تعمل دون تدخل بشري مباشر</div>
    <div class="summary-item">تشمل الأشياء الثابتة والمتنقلة</div>
    <div class="summary-item">تزيد من الكفاءة في مجالات كثيرة</div>
  </div>

  <div class="summary-card" style="border-color:rgba(52,211,153,0.3);">
    <h3 style="color:#34d399;">⚙️ مكونات النظام</h3>
    <div class="summary-item">حساسات (Sensors) تقرأ البيئة</div>
    <div class="summary-item">مشغلات (Actuators) تنفذ الأوامر</div>
    <div class="summary-item">MCU أو SBC للمعالجة والتحكم</div>
    <div class="summary-item">بوابة IoT Gateway للاتصال السحابي</div>
    <div class="summary-item">منصة سحابية للتخزين والمعالجة</div>
  </div>

  <div class="summary-card" style="border-color:rgba(129,140,248,0.3);">
    <h3 style="color:#818cf8;">📡 تقنيات الاتصال</h3>
    <div class="summary-item">Wi-Fi: الشبكة المحلية والإنترنت</div>
    <div class="summary-item">Bluetooth: الاتصال القريب</div>
    <div class="summary-item">Zigbee: المدن والزراعة الذكية</div>
    <div class="summary-item">IoT Gateway: ربط الشبكة بالسحابة</div>
  </div>

  <div class="summary-card" style="border-color:rgba(251,146,60,0.3);">
    <h3 style="color:#fb923c;">🏠 المنزل الذكي</h3>
    <div class="summary-item">التحكم عن بُعد عبر الهاتف الذكي أو الأوامر الصوتية</div>
    <div class="summary-item">التشغيل التلقائي وفق شروط محددة</div>
    <div class="summary-item">تكامل الأجهزة لتحسين الأمان والكفاءة</div>
    <div class="summary-item">أمثلة: مصابيح ذكية، قفل ذكي، ثلاجة ذكية</div>
  </div>

  <div class="summary-card" style="border-color:rgba(250,204,21,0.3);">
    <h3 style="color:#facc15;">🏗️ هيكلية الشبكة</h3>
    <div class="summary-item">طبقة الإدراك: الحساسات والمشغلات</div>
    <div class="summary-item">طبقة الشبكة: المعالجة المسبقة والحوسبة الضبابية</div>
    <div class="summary-item">طبقة التطبيق: السحابة وواجهة المستخدم</div>
  </div>

  <div class="summary-card" style="border-color:rgba(244,114,182,0.3);">
    <h3 style="color:#f472b6;">🔐 أمن IoT</h3>
    <div class="summary-item">حماية الأجهزة والشبكات من الهجمات الإلكترونية</div>
    <div class="summary-item">تحديث الأجهزة والبرامج باستمرار</div>
    <div class="summary-item">تغيير كلمات المرور دوريًا</div>
    <div class="summary-item">استخدام التشفير في نقل البيانات</div>
  </div>

  <div class="summary-card" style="border-color:rgba(52,211,153,0.3);">
    <h3 style="color:#34d399;">💾 جمع البيانات</h3>
    <div class="summary-item">توليد البيانات: أجهزة الاستشعار</div>
    <div class="summary-item">نقل البيانات: عبر بوابات IoT</div>
    <div class="summary-item">تخزين البيانات: قواعد بيانات أو سحابية</div>
  </div>

  <div class="summary-card" style="border-color:rgba(56,189,248,0.3);">
    <h3 style="color:#38bdf8;">🛠️ تصميم شبكة IoT</h3>
    <div class="summary-item">Packet Tracer لمحاكاة الشبكات</div>
    <div class="summary-item">3 سيناريوهات: Home Gateway، Server+AP، إطفاء حريق</div>
    <div class="summary-item">خطوات: تحديد المشكلة → الأجهزة → النموذج → الكتيّب</div>
    <div class="summary-item">DHCP يخصص عناوين IP تلقائيًا</div>
  </div>
</div>

<!-- Final table -->
<div class="section-heading"><span>جدول المصطلحات الأساسية</span></div>
<table class="info-table">
  <thead><tr style="background:rgba(56,189,248,0.15);">
    <th style="color:#38bdf8;">المصطلح</th><th style="color:#38bdf8;">التعريف المختصر</th>
  </tr></thead>
  <tbody>
    <tr><td>IoT</td><td>إنترنت الأشياء: شبكة أجهزة مترابطة تتشارك البيانات</td></tr>
    <tr><td>MCU (Microcontroller)</td><td>حاسوب صغير مدمج لمهام محددة مثل Arduino</td></tr>
    <tr><td>SBC (Single Board Computer)</td><td>حاسوب كامل على لوحة مثل Raspberry Pi</td></tr>
    <tr><td>Sensor (حساس)</td><td>جهاز يقرأ البيانات من البيئة ويحوّلها لإشارات رقمية</td></tr>
    <tr><td>Actuator (مشغّل)</td><td>جهاز ينفذ الأوامر ويُحدث تأثيرًا ماديًا</td></tr>
    <tr><td>Gateway (بوابة)</td><td>تربط الشبكة اللاسلكية بالسحابة الرقمية</td></tr>
    <tr><td>Fog Computing</td><td>الحوسبة الضبابية: معالجة البيانات قريبًا من مصدرها</td></tr>
    <tr><td>GPS</td><td>نظام تحديد المواقع العالمي عبر الأقمار الصناعية</td></tr>
    <tr><td>DHCP</td><td>بروتوكول يخصص عناوين IP تلقائيًا للأجهزة</td></tr>
    <tr><td>SSID</td><td>اسم الشبكة اللاسلكية المُعرِّف</td></tr>
    <tr><td>Smart Home</td><td>منزل مجهز بتقنيات للتحكم عن بُعد في أجهزته</td></tr>
    <tr><td>IoT Security</td><td>حماية الأجهزة والشبكات الذكية من الهجمات الإلكترونية</td></tr>
  </tbody>
</table>
```

  </div>
</div>

<style>
    /* 1. تنسيق الخلفية العامة والجسم */
    body {
        background: #050811 !important;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(56, 189, 248, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(129, 140, 248, 0.1) 0%, transparent 50%) !important;
        color: #e2e8f0 !important;
        line-height: 1.8 !important;
    }

    /* 2. تحويل البطاقات الأصلية إلى نمط زجاجي نيون */
    .branch, .concept-card, .lesson-hero, .summary-card, .glass-card, .sub-node {
        background: rgba(17, 25, 40, 0.75) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* تأثير الحركية عند تمرير الماوس */
    .branch:hover, .concept-card:hover, .summary-card:hover {
        transform: translateY(-10px) scale(1.02) !important;
        border-color: #38bdf8 !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.3) !important;
    }

    /* 3. تنسيق القوائم والأزرار */
    .nav-tab {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        color: #94a3b8 !important;
        padding: 10px 25px !important;
        border-radius: 50px !important;
        transition: 0.3s !important;
        cursor: pointer !important;
    }

    .nav-tab.active, .nav-tab:hover {
        background: linear-gradient(135deg, #38bdf8, #818cf8) !important;
        color: #000 !important;
        font-weight: bold !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.5) !important;
    }

    /* 4. تنسيق الجداول لتصبح عصرية */
    table, .info-table {
        width: 100% !important;
        border-radius: 15px !important;
        overflow: hidden !important;
        border: none !important;
        background: rgba(255, 255, 255, 0.02) !important;
    }

    th {
        background: rgba(56, 189, 248, 0.2) !important;
        color: #38bdf8 !important;
        padding: 15px !important;
    }

    td {
        padding: 12px !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* 5. تأثيرات النصوص */
    h1, h2, .branch-title {
        background: linear-gradient(135deg, #fff, #38bdf8) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 900 !important;
    }

    /* 6. إضافات الجمالية (النقاط المتحركة) */
    .sub-node-items li {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        padding: 5px 15px !important;
        border-radius: 20px !important;
        margin: 5px !important;
        display: inline-block !important;
        color: #38bdf8 !important;
    }
</style>

<script>
    // جافا سكريبت لتحسين التفاعل تلقائياً
    document.addEventListener('DOMContentLoaded', () => {
        // إضافة أنيميشن عند التمرير (Reveal Effect)
        const observerOptions = { threshold: 0.1 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = "1";
                    entry.target.style.transform = "translateY(0)";
                }
            });
        }, observerOptions);

        document.querySelectorAll('.section, .branch, .concept-card').forEach(el => {
            el.style.opacity = "0";
            el.style.transform = "translateY(20px)";
            el.style.transition = "all 0.6s ease-out";
            observer.observe(el);
        });

        // تحسين وظيفة فتح الفروع (إذا لم تكن موجودة)
        window.toggleBranch = function(id) {
            const branch = document.getElementById(id);
            if(branch) {
                branch.classList.toggle('open');
                const body = branch.querySelector('.branch-body');
                if(body) {
                    body.style.display = branch.classList.contains('open') ? 'block' : 'none';
                    body.style.animation = 'fadeIn 0.3s ease';
                }
            }
        };
    });
</script>

<script>
// دالة الانتقال بين الدروس (Tabs)
function showSection(id) {
    // 1. إخفاء جميع الأقسام
    const sections = document.querySelectorAll('.section');
    sections.forEach(s => {
        s.classList.remove('active');
        s.style.display = 'none';
    });

    // 2. إظهار القسم المطلوب فقط
    const targetSection = document.getElementById('section-' + id);
    if (targetSection) {
        targetSection.style.display = 'block';
        // إضافة تأخير بسيط لتفعيل التأنيمشن
        setTimeout(() => {
            targetSection.classList.add('active');
        }, 10);
    }

    // 3. تحديث شكل الأزرار (Tabs)
    const tabs = document.querySelectorAll('.nav-tab');
    tabs.forEach(t => {
        t.classList.remove('active');
        t.style.background = 'transparent'; // إعادة اللون الشفاف
    });

    // 4. تلوين الزر المضغوط
    const activeTab = document.getElementById('tab-' + id);
    if (activeTab) {
        activeTab.classList.add('active');
        activeTab.style.background = '#38bdf8'; // لون التمييز
    }

    // 5. العودة لأعلى الصفحة عند الانتقال
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// دالة فتح وإغلاق الفروع في الخريطة الذهنية
function toggleBranch(id) {
    const branch = document.getElementById(id);
    if (branch) {
        branch.classList.toggle('open');
        const body = branch.querySelector('.branch-body');
        const toggleBtn = branch.querySelector('.branch-toggle');
        
        if (branch.classList.contains('open')) {
            body.style.display = 'block';
            toggleBtn.innerText = '−';
            branch.style.borderColor = '#38bdf8';
        } else {
            body.style.display = 'none';
            toggleBtn.innerText = '+';
            branch.style.borderColor = 'rgba(99,179,237,0.15)';
        }
    }
}

// تنفيذ عند تشغيل الصفحة لأول مرة لضمان ظهور أول قسم
document.addEventListener('DOMContentLoaded', () => {
    showSection('mindmap'); 
});
</script>
<style>
    /* إضافة لمسة للاسم في الهيدر */
    header p::after {
        content: " | إعداد الأستاذ أحمد نزال";
        color: #38bdf8;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }

    /* تنسيق الفوتر الأسفل */
    .teacher-footer {
        text-align: center;
        padding: 30px;
        margin-top: 50px;
        border-top: 1px solid rgba(56, 189, 248, 0.2);
        background: rgba(10, 15, 30, 0.8);
        backdrop-filter: blur(10px);
    }

    .teacher-name {
        font-family: 'Tajawal', sans-serif;
        font-size: 18px;
        background: linear-gradient(135deg, #fff, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* تحسين التنقل (Tabs) لإصلاح مشكلة التعليق */
    .section { display: none; opacity: 0; transform: translateY(20px); transition: all 0.5s ease; }
    .section.active { display: block; opacity: 1; transform: translateY(0); }
</style>

<footer class="teacher-footer">
    <div class="teacher-name">تم إعداد هذا الملخص بواسطة الأستاذ أحمد نزال ✨</div>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 5px;">كل التوفيق للطلبة المتميزين</p>
</footer>

<script>
// دالة التنقل بين الدروس - الأستاذ أحمد نزال
function showSection(id) {
    // 1. إخفاء جميع الأقسام
    const sections = document.querySelectorAll('.section');
    sections.forEach(s => {
        s.classList.remove('active');
        s.style.display = 'none';
    });

    // 2. إظهار القسم المطلوب
    const target = document.getElementById('section-' + id);
    if (target) {
        target.style.display = 'block';
        setTimeout(() => { target.classList.add('active'); }, 50);
    }

    // 3. تحديث شكل الأزرار
    const tabs = document.querySelectorAll('.nav-tab');
    tabs.forEach(t => {
        t.classList.remove('active');
        t.style.background = 'transparent';
        t.style.color = '#94a3b8';
    });

    // 4. تمييز الزر النشط
    const activeTab = document.getElementById('tab-' + id);
    if (activeTab) {
        activeTab.classList.add('active');
        activeTab.style.background = '#38bdf8';
        activeTab.style.color = '#000';
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// دالة فتح وإغلاق الفروع
function toggleBranch(id) {
    const branch = document.getElementById(id);
    if (branch) {
        branch.classList.toggle('open');
        const body = branch.querySelector('.branch-body');
        const toggleBtn = branch.querySelector('.branch-toggle');
        
        if (branch.classList.contains('open')) {
            body.style.display = 'block';
            toggleBtn.innerText = '−';
        } else {
            body.style.display = 'none';
            toggleBtn.innerText = '+';
        }
    }
}

// تشغيل الصفحة على أول قسم تلقائياً
document.addEventListener('DOMContentLoaded', () => {
    showSection('mindmap');
});
</script>
</body>

</html>
