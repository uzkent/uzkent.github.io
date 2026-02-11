```markdown
---
title: ""
permalink: /publications/
author_profile: true
redirect_from:
  - /publications
---

{% include base_path %}

<style>
/* ===== Global Styles ===== */
.pub-page {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 960px;
  margin: 0 auto;
}

/* ===== Hero Header ===== */
.pub-hero {
  background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
  color: #fff;
  padding: 2.5rem 2rem;
  border-radius: 16px;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  position: relative;
  overflow: hidden;
}

.pub-hero::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 70%);
  animation: shimmer 8s ease-in-out infinite;
}

@keyframes shimmer {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(5%, 5%); }
}

.pub-hero h1 {
  font-size: 2.4rem;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.5px;
  position: relative;
  z-index: 1;
}

.pub-hero h1 .emoji-icon {
  font-size: 2rem;
}

.pub-hero .subtitle {
  font-size: 1.05rem;
  opacity: 0.88;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
  position: relative;
  z-index: 1;
}

/* ===== Stats Bar ===== */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 1rem;
  margin: 1.8rem auto 0 auto;
  max-width: 750px;
  position: relative;
  z-index: 1;
}

.stat-card {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 1rem 0.5rem;
  text-align: center;
  transition: transform 0.2s ease, background 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-3px);
  background: rgba(255,255,255,0.18);
}

.stat-number {
  font-size: 1.8rem;
  font-weight: 800;
  display: block;
  background: linear-gradient(135deg, #74ebd5, #ACB6E5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.85;
  margin-top: 0.2rem;
  display: block;
}

/* ===== Venue Badges (Marquee) ===== */
.venue-marquee {
  margin: 1.5rem 0;
  overflow: hidden;
  position: relative;
}

.venue-marquee::before,
.venue-marquee::after {
  content: '';
  position: absolute;
  top: 0;
  width: 60px;
  height: 100%;
  z-index: 2;
}

.venue-marquee::before {
  left: 0;
  background: linear-gradient(to right, #fff, transparent);
}

.venue-marquee::after {
  right: 0;
  background: linear-gradient(to left, #fff, transparent);
}

.venue-track {
  display: flex;
  gap: 0.6rem;
  animation: scrollVenues 30s linear infinite;
  width: max-content;
}

@keyframes scrollVenues {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.venue-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.85rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  white-space: nowrap;
  border: 1.5px solid;
}

.venue-badge.tier-s { background: #fef3c7; color: #92400e; border-color: #f59e0b; }
.venue-badge.tier-a { background: #dbeafe; color: #1e40af; border-color: #3b82f6; }
.venue-badge.tier-b { background: #f0fdf4; color: #166534; border-color: #22c55e; }
.venue-badge.tier-j { background: #fdf2f8; color: #9d174d; border-color: #ec4899; }

.badge-count {
  background: rgba(0,0,0,0.1);
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.4rem;
  font-size: 0.7rem;
}

/* ===== Section Headers ===== */
.section-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin: 2.5rem 0 1.2rem 0;
  padding-bottom: 0.6rem;
  border-bottom: 3px solid;
  border-image: linear-gradient(90deg, #3b82f6, #8b5cf6, transparent) 1;
}

.section-icon {
  font-size: 1.6rem;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #eff6ff, #ede9fe);
  border-radius: 12px;
  flex-shrink: 0;
}

.section-header h2 {
  margin: 0;
  font-size: 1.5rem;
  color: #1e293b;
  letter-spacing: -0.3px;
}

.section-header .paper-count {
  margin-left: auto;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
}

/* ===== Year Dividers ===== */
.year-divider {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 2rem 0 1rem 0;
}

.year-pill {
  background: linear-gradient(135deg, #1e293b, #334155);
  color: #fff;
  padding: 0.4rem 1.2rem;
  border-radius: 20px;
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: 1px;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(30,41,59,0.2);
}

.year-line {
  flex: 1;
  height: 2px;
  background: linear-gradient(to right, #cbd5e1, transparent);
  border-radius: 1px;
}

/* ===== Paper Cards ===== */
.paper-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #3b82f6;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.25s ease;
  position: relative;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.paper-card:hover {
  transform: translateX(4px);
  box-shadow: 0 6px 24px rgba(0,0,0,0.08);
  border-left-color: #8b5cf6;
}

.paper-card.journal {
  border-left-color: #ec4899;
}

.paper-card.journal:hover {
  border-left-color: #f43f5e;
}

.paper-card.preprint {
  border-left-color: #6366f1;
  border-style: solid solid solid dashed;
}

.paper-number {
  position: absolute;
  top: -0.5rem;
  right: 1rem;
  background: #f1f5f9;
  color: #64748b;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 8px;
  letter-spacing: 0.5px;
}

.paper-venue {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  padding: 0.2rem 0.6rem;
  border-radius: 6px;
  margin-bottom: 0.5rem;
}

.paper-venue.cvpr { background: #fef3c7; color: #92400e; }
.paper-venue.iccv { background: #fef3c7; color: #92400e; }
.paper-venue.iclr { background: #fee2e2; color: #991b1b; }
.paper-venue.aaai { background: #dbeafe; color: #1e40af; }
.paper-venue.ijcai { background: #e0e7ff; color: #3730a3; }
.paper-venue.kdd { background: #fce7f3; color: #9d174d; }
.paper-venue.wacv { background: #f0fdf4; color: #166534; }
.paper-venue.workshop { background: #f5f3ff; color: #5b21b6; }
.paper-venue.journal { background: #fdf2f8; color: #9d174d; }
.paper-venue.preprint { background: #f1f5f9; color: #475569; }

.oral-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  background: linear-gradient(135deg, #dc2626, #ef4444);
  color: #fff;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 0.15rem 0.55rem;
  border-radius: 6px;
  margin-left: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.4); }
  50% { box-shadow: 0 0 0 6px rgba(239,68,68,0); }
}

.paper-title {
  font-size: 1rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0.3rem 0;
  line-height: 1.45;
}

.paper-authors {
  font-size: 0.85rem;
  color: #475569;
  margin: 0.3rem 0;
  line-height: 1.5;
}

.paper-authors .me {
  font-weight: 700;
  color: #1e293b;
  background: linear-gradient(135deg, #dbeafe, #ede9fe);
  padding: 0.05rem 0.35rem;
  border-radius: 4px;
}

.paper-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.6rem;
}

.paper-link {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.25rem 0.65rem;
  font-size: 0.72rem;
  font-weight: 600;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 1px solid;
}

.paper-link.pdf { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
.paper-link.pdf:hover { background: #2563eb; color: #fff; }
.paper-link.arxiv { background: #fef3c7; color: #d97706; border-color: #fde68a; }
.paper-link.arxiv:hover { background: #d97706; color: #fff; }
.paper-link.code { background: #f0fdf4; color: #16a34a; border-color: #bbf7d0; }
.paper-link.code:hover { background: #16a34a; color: #fff; }
.paper-link.project { background: #fdf2f8; color: #db2777; border-color: #fbcfe8; }
.paper-link.project:hover { background: #db2777; color: #fff; }

/* ===== Timeline Connector ===== */
.timeline-container {
  position: relative;
  padding-left: 1.5rem;
}

.timeline-container::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, #3b82f6, #8b5cf6, #ec4899, #f59e0b, #22c55e);
  border-radius: 2px;
}

.timeline-dot {
  position: absolute;
  left: -1.5rem;
  top: 1.5rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid #3b82f6;
  z-index: 1;
  margin-left: -4.5px;
}

/* ===== Footer Summary ===== */
.pub-footer {
  background: linear-gradient(135deg, #f8fafc, #eff6ff, #faf5ff);
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  margin-top: 3rem;
  position: relative;
  overflow: hidden;
}

.pub-footer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #f59e0b);
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  max-width: 500px;
  margin: 0 auto;
}

.footer-stat {
  text-align: center;
}

.footer-number {
  font-size: 2.2rem;
  font-weight: 900;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-label {
  font-size: 0.8rem;
  color: #64748b;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.equal-note {
  margin-top: 1.2rem;
  font-size: 0.8rem;
  color: #94a3b8;
  font-style: italic;
}

/* ===== Responsive ===== */
@media (max-width: 640px) {
  .pub-hero { padding: 1.5rem 1rem; }
  .pub-hero h1 { font-size: 1.6rem; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .paper-card { padding: 1rem; }
  .footer-grid { grid-template-columns: 1fr; }
}
</style>

<div class="pub-page">

<!-- ==================== HERO ==================== -->
<div class="pub-hero">
  <h1><span class="emoji-icon">📚</span> Publications</h1>
  <p class="subtitle">
    Research spanning <strong>computer vision</strong>, <strong>efficient deep learning</strong>, <strong>multi-modal models</strong>, and <strong>remote sensing</strong> — published at top-tier venues worldwide.
  </p>
  <div class="stats-grid">
    <div class="stat-card">
      <span class="stat-number">43</span>
      <span class="stat-label">Total Papers</span>
    </div>
    <div class="stat-card">
      <span class="stat-number">9</span>
      <span class="stat-label">Journal Articles</span>
    </div>
    <div class="stat-card">
      <span class="stat-number">29</span>
      <span class="stat-label">Conference Papers</span>
    </div>
    <div class="stat-card">
      <span class="stat-number">5</span>
      <span class="stat-label">Preprints</span>
    </div>
  </div>
</div>

<!-- ==================== VENUE MARQUEE ==================== -->
<div class="venue-marquee">
  <div class="venue-track">
    <span class="venue-badge tier-s">🏆 CVPR <span class="badge-count">3</span></span>
    <span class="venue-badge tier-s">🏆 ICCV <span class="badge-count">1</span></span>
    <span class="venue-badge tier-s">🏆 ICLR <span class="badge-count">2</span></span>
    <span class="venue-badge tier-a">⭐ AAAI <span class="badge-count">3</span></span>
    <span class="venue-badge tier-a">⭐ IJCAI <span class="badge-count">2</span></span>
    <span class="venue-badge tier-a">⭐ KDD <span class="badge-count">1</span></span>
    <span class="venue-badge tier-b">🔬 WACV <span class="badge-count">5</span></span>
    <span class="venue-badge tier-b">🔬 CVPRW <span class="badge-count">3</span></span>
    <span class="venue-badge tier-j">📖 IEEE TGRS</span>
    <span class="venue-badge tier-j">📖 IEEE Sensors</span>
    <span class="venue-badge tier-j">📖 Earth's Future</span>
    <!-- duplicate for seamless loop -->
    <span class="venue-badge tier-s">🏆 CVPR <span class="badge-count">3</span></span>
    <span class="venue-badge tier-s">🏆 ICCV <span class="badge-count">1</span></span>
    <span class="venue-badge tier-s">🏆 ICLR <span class="badge-count">2</span></span>
    <span class="venue-badge tier-a">⭐ AAAI <span class="badge-count">3</span></span>
    <span class="venue-badge tier-a">⭐ IJCAI <span class="badge-count">2</span></span>
    <span class="venue-badge tier-a">⭐ KDD <span class="badge-count">1</span></span>
    <span class="venue-badge tier-b">🔬 WACV <span class="badge-count">5</span></span>
    <span class="venue-badge tier-b">🔬 CVPRW <span class="badge-count">3</span></span>
    <span class="venue-badge tier-j">📖 IEEE TGRS</span>
    <span class="venue-badge tier-j">📖 IEEE Sensors</span>
    <span class="venue-badge tier-j">📖 Earth's Future</span>
  </div>
</div>

<!-- ============================================================ -->
<!--                     CONFERENCE PAPERS                        -->
<!-- ============================================================ -->

<div class="section-header">
  <div class="section-icon">🎤</div>
  <h2>Peer-Reviewed Conference Papers</h2>
  <span class="paper-count">29 papers</span>
</div>

<div class="timeline-container">

<!-- ────── 2024 ────── -->
<div class="year-divider">
  <span class="year-pill">2024</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#1</span>
  <div class="paper-venue wacv">📷 WACV 2024</div>
  <div class="paper-title">A Multimodal Benchmark and Improved Architecture for Zero Shot Learning</div>
  <div class="paper-authors">K. Doshi, A. Garg, <span class="me">B. Uzkent</span>, X. Wang, M. Omar</div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#2</span>
  <div class="paper-venue wacv">📷 WACV 2024</div>
  <div class="paper-title">Augment the Pairs: Semantics-Preserving Image-Caption Pair Augmentation for Grounding-Based Vision and Language Models</div>
  <div class="paper-authors">J. Yi, <span class="me">B. Uzkent</span>, O. Ignat, Z. Li, A. Garg, X. Yu, L. Liu</div>
</div>

<!-- ────── 2023 ────── -->
<div class="year-divider">
  <span class="year-pill">2023</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#3</span>
  <div class="paper-venue cvpr">🏆 CVPR 2023</div>
  <div class="paper-title">Dynamic Inference with Grounding Based Vision and Language Models</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Garg, W. Zhou, K. Doshi, J. Yi, X. Wang, M. Omar</div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#4</span>
  <div class="paper-venue aaai">⭐ AAAI 2023</div>
  <div class="paper-title">GOHSP: A Unified Framework of Graph and Optimization-based Heterogeneous Structured Pruning for Vision Transformer</div>
  <div class="paper-authors">M. Yin, <span class="me">B. Uzkent</span>, Y. Shen, H. Jin</div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#5</span>
  <div class="paper-venue iclr">🧠 ICLR 2023</div>
  <div class="paper-title">Learning to Jointly Share and Prune Weights for Grounding Based Vision and Language Models</div>
  <div class="paper-authors">S. Gao, <span class="me">B. Uzkent</span>, Y. Shen, H. Huang, H. Jin</div>
</div>

<!-- ────── 2022 ────── -->
<div class="year-divider">
  <span class="year-pill">2022</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#6</span>
  <div class="paper-venue workshop">🔬 CVPRW 2022</div>
  <div class="paper-title">Efficient Conditional Pre-training for Transfer Learning</div>
  <div class="paper-authors">S. Chakraborty, <span class="me">B. Uzkent</span>, K. Ayush, E. Sheehan, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2011.10231" class="paper-link arxiv">📄 arXiv</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#7</span>
  <div class="paper-venue cvpr">🏆 CVPR 2022</div>
  <div class="paper-title">Lite-MDETR: A Lightweight Multi-Modal Detector</div>
  <div class="paper-authors">Q. Lu, Y.C. Shu, <span class="me">B. Uzkent</span>, T. Hua, Y. Shen, H. Jin</div>
</div>

<!-- ────── 2021 ────── -->
<div class="year-divider">
  <span class="year-pill">2021</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#8</span>
  <div class="paper-venue iccv">🏆 ICCV 2021</div>
  <div class="paper-title">Geography-Aware Self-Supervised Learning</div>
  <div class="paper-authors">K. Ayush, <span class="me">B. Uzkent</span>, C. Meng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Ayush_Geography-Aware_Self-Supervised_Learning_ICCV_2021_paper.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/sustainlab-group/geography-aware-ssl" class="paper-link code">💻 Code</a>
    <a href="https://geography-aware-ssl.github.io/" class="paper-link project">🌐 Project</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#9</span>
  <div class="paper-venue iclr">🧠 ICLR 2021</div>
  <div class="paper-title">Negative Data Augmentation</div>
  <div class="paper-authors">K. Ayush*, A. Sinha*, J. Song, <span class="me">B. Uzkent</span>, H. Jin, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openreview.net/forum?id=Ovp8dvB8IBH" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/ermongroup/NDA" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#10</span>
  <div class="paper-venue aaai">⭐ AAAI 2021</div>
  <div class="paper-title">Efficient High Resolution Image Processing using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, K. Ayush, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2006.04224.pdf" class="paper-link arxiv">📄 arXiv</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#11</span>
  <div class="paper-venue aaai">⭐ AAAI 2021</div>
  <div class="paper-title">Predicting Geo-attributes Using Deep Learning and Publicly Available Street-level Images</div>
  <div class="paper-authors">J. Lee, D. Grosz, <span class="me">B. Uzkent</span>, S. Zheng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2006.08661.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://github.com/sustainlab-group/mapillarygcn" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2020 ────── -->
<div class="year-divider">
  <span class="year-pill">2020</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#12</span>
  <div class="paper-venue ijcai">⭐ IJCAI 2020</div>
  <div class="paper-title">Generating Interpretable Poverty Maps Using Object Detection in Satellite Images</div>
  <div class="paper-authors">K. Ayush, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2002.01612.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://www.ijcai.org/Proceedings/2020/0608.pdf" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#13</span>
  <div>
    <span class="paper-venue cvpr">🏆 CVPR 2020</span>
    <span class="oral-badge">🎯 Oral</span>
  </div>
  <div class="paper-title">Learning When and Where to Zoom Using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2003.00425.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Uzkent_Learning_When_and_Where_to_Zoom_With_Deep_Reinforcement_Learning_CVPR_2020_paper.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/ermongroup/PatchDrop" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#14</span>
  <div class="paper-venue workshop">🔬 CVPRW 2020</div>
  <div class="paper-title">Farmland Parcel Delineation using Spatio-temporal Convolutional Networks</div>
  <div class="paper-authors">H.L. Aung, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/sustainlab-group/ParcelDelineation" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#15</span>
  <div class="paper-venue wacv">📷 WACV 2020</div>
  <div class="paper-title">Cloud Removal from Satellite Images Using Spatiotemporal Generator Networks</div>
  <div class="paper-authors">V. Sarukkai, A. Jain, <span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1912.06838.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/VSAnimator/stgan" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#16</span>
  <div class="paper-venue wacv">📷 WACV 2020</div>
  <div class="paper-title">Efficient Object Detection in Large Images Using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, C. Yeh, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1912.03966.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Uzkent_Efficient_Object_Detection_in_Large_Images_Using_Deep_Reinforcement_Learning_WACV_2020_paper.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/uzkent/EfficientObjectDetection" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2019 ────── -->
<div class="year-divider">
  <span class="year-pill">2019</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#17</span>
  <div class="paper-venue ijcai">⭐ IJCAI 2019</div>
  <div class="paper-title">Learning How to Interpret Satellite Images using Wikipedia</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, D. Lobell, M. Burke, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/1905.02506" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://www.ijcai.org/proceedings/2019/0502.pdf" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/WikiSatNet" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#18</span>
  <div class="paper-venue" style="background:#fce7f3;color:#9d174d;">⭐ KDD 2019</div>
  <div class="paper-title">Predicting Economic Development using Geolocated Wikipedia Articles</div>
  <div class="paper-authors">E. Sheehan, C. Meng, M. Tan, <span class="me">B. Uzkent</span>, N. Jean, D. Lobell, M. Burke, S. Ermon</div>
  <div class="paper-links">
    <a href="https://dl.acm.org/citation.cfm?id=3330784" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/WikipediaPovertyMapping" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2018 ────── -->
<div class="year-divider">
  <span class="year-pill">2018</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#19</span>
  <div class="paper-venue wacv">📷 WACV 2018</div>
  <div class="paper-title">EnKCF: Ensemble of Kernelized Correlation Filters for High-Speed Object Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, Y. Seo</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8354233" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/EnKCF_Tracking_WACV18" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2017 ────── -->
<div class="year-divider">
  <span class="year-pill">2017</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#20</span>
  <div class="paper-venue workshop">🔬 CVPRW 2017</div>
  <div class="paper-title">Aerial Vehicle Tracking by Adaptive Fusion of Likelihood Maps</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Rangnekar, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8014769/" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2016 ────── -->
<div class="year-divider">
  <span class="year-pill">2016</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#21</span>
  <div class="paper-venue workshop">🔬 CVPRW 2016</div>
  <div class="paper-title">Real-time Target Detection and Tracking in Aerial Video using Hyperspectral Features</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/7789671" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2015 ────── -->
<div class="year-divider">
  <span class="year-pill">2015</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#22</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">ICCS 2015</div>
  <div class="paper-title">Spectral Validation of Measurements in a Vehicle Tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://www.sciencedirect.com/science/article/pii/S1877050915011667" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#23</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">SPIE 2015</div>
  <div class="paper-title">Background Image Understanding and Adaptive Imaging for Vehicle Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9460/94600F/Background-image-understanding-and-adaptive-imaging-for-vehicle-tracking/10.1117/12.2177334.short" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#24</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">SPIE 2015</div>
  <div class="paper-title">Efficient Integration of Spectral Features for Vehicle Tracking utilizing an Adaptive Sensor</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9407/1/Efficient-integration-of-spectral-features-for-vehicle-tracking-utilizing-an/10.1117/12.2082266.short" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<!-- ────── 2014 ────── -->
<div class="year-divider">
  <span class="year-pill">2014</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#25</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">IEEE WNYIPW 2014</div>
  <div class="paper-title">3-D MRI Cardiac Segmentation using Graph Cuts</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, E. Cherry, N. Cahill</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/6999484" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/3D_MRI_Segmentation" class="paper-link code">💻 Code</a>
  </div>
</div>

<!-- ────── 2013 ────── -->
<div class="year-divider">
  <span class="year-pill">2013</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#26</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">ICCS 2013</div>
  <div class="paper-title">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="paper-links">
    <a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<!-- ────── 2011 ────── -->
<div class="year-divider">
  <span class="year-pill">2011</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#27</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">IEEE ITNG 2011</div>
  <div class="paper-title">Pitch range-based feature extraction for audio surveillance systems</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana</div>
  <div class="paper-links">
    <a href="https://www.researchgate.net/profile/Buket_Barkana/publication/224245542_Pitch-Range_Based_Feature_Extraction_for_Audio_Surveillance_Systems/links/5654aa9808ae4988a7b055f7/Pitch-Range-Based-Feature-Extraction-for-Audio-Surveillance-Systems.pdf" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<!-- ────── 2010 ────── -->
<div class="year-divider">
  <span class="year-pill">2010</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#28</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">EURO 2010</div>
  <div class="paper-title">Performances of the ANN, SVM, and K-means clustering methods recognizing different environmental sounds</div>
  <div class="paper-authors">B.D. Barkana, I. Saricicek, <span class="me">B. Uzkent</span></div>
</div>

<!-- ────── 2009 ────── -->
<div class="year-divider">
  <span class="year-pill">2009</span>
  <span class="year-line"></span>
</div>

<div class="paper-card" style="position:relative;">
  <span class="paper-number">#29</span>
  <div class="paper-venue" style="background:#f1f5f9;color:#475569;">METU 2009</div>
  <div class="paper-title">Autonomous parallel parking of non-holonomic vehicles</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, O. Parlaktuna</div>
</div>

</div><!-- end timeline-container -->

<!-- ============================================================ -->
<!--                       JOURNAL PAPERS                         -->
<!-- ============================================================ -->

<div class="section-header">
  <div class="section-icon">📖</div>
  <h2>Peer-Reviewed Journal Papers</h2>
  <span class="paper-count">9 papers</span>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J1</span>
  <div class="paper-venue journal">📖 Earth's Future · 2022</div>
  <div class="paper-title">Safe Shelter: A Case for Prioritizing Housing Quality in Climate Adaptation Policy by Remotely Sensing Roof Tarps in the San Francisco Bay Area</div>
  <div class="paper-authors">E. Velterop, <span class="me">B. Uzkent</span>, J. Suckale</div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J2</span>
  <div class="paper-venue journal">📖 IEEE TGRS · 2019</div>
  <div class="paper-title">Tracking in Aerial Hyperspectral Videos using Deep Kernelized Correlation Filters</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Rangnekar, M.J. Hoffman</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8435971" class="paper-link pdf">📄 PDF</a>
    <a href="https://arxiv.org/pdf/1711.07235.pdf" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://github.com/buzkent86/HKCF_Tracker" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J3</span>
  <div class="paper-venue journal">📖 IEEE JSTARS · 2016</div>
  <div class="paper-title">Integrating Hyperspectral Likelihoods in a Multi-dimensional Assignment Algorithm for Aerial Vehicle Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/7471414" class="paper-link pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="paper-link code">💻 Code</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J4</span>
  <div class="paper-venue journal">📖 IEEE Sensors J. · 2015</div>
  <div class="paper-title">Feature Matching with an Adaptive Optical Sensor in a Ground Target Tracking System</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, Bin Chen</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/6873232/" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J5</span>
  <div class="paper-venue journal">📖 Procedia CS · 2013</div>
  <div class="paper-title">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="paper-links">
    <a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J6</span>
  <div class="paper-venue journal">📖 IJICIC · 2012</div>
  <div class="paper-title">Non-speech environmental sound classification using SVMS with a new set of features</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana, H. Cevikalp</div>
  <div class="paper-links">
    <a href="https://www.researchgate.net/profile/Hakan_Cevikalp/publication/267782696_Non-speech_environmental_sound_classification_using_SVMs_with_a_new_set_of_features/links/54b7bf9f0cf24eb34f6ed7ff/Non-speech-environmental-sound-classification-using-SVMs-with-a-new-set-of-features.pdf" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J7</span>
  <div class="paper-venue journal">📖 Adv. Mat. Research · 2012</div>
  <div class="paper-title">Normal and abnormal non-speech audio event detection using MFCC and PR-based feature sets</div>
  <div class="paper-authors">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J8</span>
  <div class="paper-venue journal">📖 Applied Acoustics · 2011</div>
  <div class="paper-title">Environmental noise classifier using a new set of feature parameters based on pitch range</div>
  <div class="paper-authors">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
  <div class="paper-links">
    <a href="https://www.sciencedirect.com/science/article/abs/pii/S0003682X11001381" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<div class="paper-card journal" style="position:relative;">
  <span class="paper-number">J9</span>
  <div class="paper-venue journal">📖 Expert Syst. w/ App. · 2011</div>
  <div class="paper-title">Automatic environmental noise source classification model using fuzzy logic</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana, J. Yang</div>
  <div class="paper-links">
    <a href="https://www.sciencedirect.com/science/article/pii/S0957417411001047" class="paper-link pdf">📄 PDF</a>
  </div>
</div>

<!-- ============================================================ -->
<!--                  PREPRINTS & TECH REPORTS                    -->
<!-- ============================================================ -->

<div class="section-header">
  <div class="section-icon">📝</div>
  <h2>Preprints &amp; Technical Reports</h2>
  <span class="paper-count">5 papers</span>
</div>

<div class="paper-card preprint" style="position:relative;">
  <span class="paper-number">P1</span>
  <div class="paper-venue preprint">📝 arXiv · 2025</div>
  <div class="paper-title">CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models</div>
  <div class="paper-authors">T. Poppi, <span class="me">B. Uzkent</span>, A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, R. Cucchiara, F. Schiffers</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2601.04778" class="paper-link arxiv">📄 arXiv</a>
  </div>
</div>

<div class="paper-card preprint" style="position:relative;">
  <span class="paper-number">P2</span>
  <div class="paper-venue preprint">📝 arXiv · 2025</div>
  <div class="paper-title">From Frames to Clips: Efficient Key Clip Selection for Long-Form Video Understanding</div>
  <div class="paper-authors">G. Sun, A. Singhal, <span class="me">B. Uzkent</span>, M. Shah, C. Chen, G. Kessler</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2510.02262" class="paper-link arxiv">📄 arXiv</a>
    <a href="https://guangyusun.com/f2c/" class="paper-link project">🌐 Project</a>
  </div>
</div>

<div class="paper-card preprint" style="position:relative;">
  <span class="paper-number">P3</span>
  <div class="paper-venue preprint">📝 Preprint</div>
  <div class="paper-title">Domain Adaptation Using Adversarial Learning for Studying Low Resolution Images</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links">
    <a href="https://www.researchgate.net/publication/341030568_Adversarial_Domain_Adaptation_for_Analyzing_Low_Resolution_Images" class="paper-link arxiv">📄 ResearchGate</a>
  </div>
</div>

<div class="paper-card preprint" style="position:relative;">
  <span class="paper-number">P4</span>
  <div class="paper-venue preprint">📝 arXiv</div>
  <div class="paper-title">Learning to Interpret Satellite Images in Global Scale Using Wikipedia</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1905.02506.pdf" class="paper-link arxiv">📄 arXiv</a>
  </div>
</div>

<div class="paper-card preprint" style="position:relative;">
  <span class="paper-number">P5</span>
  <div class="paper-venue preprint">📝 arXiv</div>
  <div class="paper-title">Learning to interpret satellite images using wikipedia</div>
  <div class="paper-authors">E. Sheehan, <span class="me">B. Uzkent</span>, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1809.10236.pdf" class="paper-link arxiv">📄 arXiv</a>
  </div>
</div>

<!-- ==================== FOOTER SUMMARY ==================== -->
<div class="pub-footer">
  <div class="footer-grid">
    <div class="footer-stat">
      <div class="footer-number">9</div>
      <div class="footer-label">Journal Papers</div>
    </div>
    <div class="footer-stat">
      <div class="footer-number">29</div>
      <div class="footer-label">Conference Papers</div>
    </div>
    <div class="footer-stat">
      <div class="footer-number">5</div>
      <div class="footer-label">Preprints</div>
    </div>
  </div>
  <p class="equal-note">* denotes equal contribution</p>
</div>

</div><!-- end pub-page -->
```
