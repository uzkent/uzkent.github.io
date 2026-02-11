

```markdown
---
title: "Publications"
permalink: /publications/
author_profile: true
redirect_from:
  - /publications
---

{% include base_path %}

<style>
.pub-hero {
  background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
  color: #fff;
  padding: 2.5rem 2rem;
  border-radius: 16px;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
}
.pub-hero h1 { font-size: 2.2rem; margin: 0 0 0.5rem 0; }
.pub-hero .subtitle { font-size: 1rem; opacity: 0.88; max-width: 700px; margin: 0 auto; line-height: 1.6; }
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
  margin: 1.5rem auto 0 auto;
  max-width: 700px;
}
.stat-card {
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 0.8rem 0.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.25s ease;
  text-decoration: none;
  color: #fff;
  display: block;
}
.stat-card:hover {
  background: rgba(255,255,255,0.22);
  transform: translateY(-3px);
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  text-decoration: none;
  color: #fff;
}
.stat-card:active { transform: translateY(-1px); }
.stat-number {
  font-size: 1.8rem;
  font-weight: 800;
  color: #74ebd5;
}
.stat-label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.85;
}
.stat-hint {
  font-size: 0.55rem;
  opacity: 0.5;
  margin-top: 0.2rem;
  letter-spacing: 0.5px;
}
.venue-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin: 1.5rem 0;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}
.vb {
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.7rem;
  border-radius: 20px;
  font-size: 0.73rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  border: 1.5px solid;
}
.vb-s { background: #fef3c7; color: #92400e; border-color: #f59e0b; }
.vb-a { background: #dbeafe; color: #1e40af; border-color: #3b82f6; }
.vb-b { background: #f0fdf4; color: #166534; border-color: #22c55e; }
.vb-j { background: #fdf2f8; color: #9d174d; border-color: #ec4899; }
.bc {
  background: rgba(0,0,0,0.08);
  border-radius: 50%;
  width: 18px; height: 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.3rem;
  font-size: 0.65rem;
}

/* Quick‑nav bar */
.quick-nav {
  display: flex;
  justify-content: center;
  gap: 0.8rem;
  margin: 0 0 2rem 0;
  flex-wrap: wrap;
}
.quick-nav a {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.55rem 1.2rem;
  border-radius: 10px;
  font-size: 0.82rem;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 2px solid;
}
.quick-nav a:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.qn-conf { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
.qn-conf:hover { background: #2563eb; color: #fff; }
.qn-jour { background: #fdf2f8; color: #db2777; border-color: #fbcfe8; }
.qn-jour:hover { background: #db2777; color: #fff; }
.qn-pre  { background: #f5f3ff; color: #7c3aed; border-color: #ddd6fe; }
.qn-pre:hover  { background: #7c3aed; color: #fff; }

.section-header {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  margin: 2.5rem 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 3px solid;
  border-image: linear-gradient(90deg, #3b82f6, #8b5cf6, transparent) 1;
  scroll-margin-top: 80px;
}
.section-icon {
  font-size: 1.5rem;
  width: 44px; height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #eff6ff, #ede9fe);
  border-radius: 10px;
}
.section-header h2 { margin: 0; font-size: 1.4rem; color: #1e293b; }
.pc {
  margin-left: auto;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.2rem 0.7rem;
  border-radius: 20px;
}
.year-div {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 1.8rem 0 0.8rem 0;
}
.year-pill {
  background: linear-gradient(135deg, #1e293b, #334155);
  color: #fff;
  padding: 0.35rem 1.1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 800;
  letter-spacing: 1px;
  box-shadow: 0 2px 8px rgba(30,41,59,0.2);
}
.year-line {
  flex: 1;
  height: 2px;
  background: linear-gradient(to right, #cbd5e1, transparent);
}
.paper {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #3b82f6;
  border-radius: 10px;
  padding: 1.1rem 1.3rem;
  margin-bottom: 0.8rem;
  transition: all 0.2s ease;
  position: relative;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.paper:hover {
  transform: translateX(4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  border-left-color: #8b5cf6;
}
.paper.jnl { border-left-color: #ec4899; }
.paper.jnl:hover { border-left-color: #f43f5e; }
.paper.pre { border-left-color: #6366f1; border-left-style: dashed; }
.pnum {
  position: absolute;
  top: -0.4rem; right: 0.8rem;
  background: #f1f5f9;
  color: #64748b;
  font-size: 0.6rem;
  font-weight: 700;
  padding: 0.1rem 0.45rem;
  border-radius: 6px;
}
.pv {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.7px;
  padding: 0.18rem 0.55rem;
  border-radius: 5px;
  margin-bottom: 0.35rem;
}
.pv-cvpr { background: #fef3c7; color: #92400e; }
.pv-iccv { background: #fef3c7; color: #92400e; }
.pv-iclr { background: #fee2e2; color: #991b1b; }
.pv-aaai { background: #dbeafe; color: #1e40af; }
.pv-ijcai { background: #e0e7ff; color: #3730a3; }
.pv-kdd { background: #fce7f3; color: #9d174d; }
.pv-wacv { background: #f0fdf4; color: #166534; }
.pv-ws { background: #f5f3ff; color: #5b21b6; }
.pv-jnl { background: #fdf2f8; color: #9d174d; }
.pv-pre { background: #f1f5f9; color: #475569; }
.pv-other { background: #f1f5f9; color: #475569; }
.oral {
  display: inline-block;
  background: linear-gradient(135deg, #dc2626, #ef4444);
  color: #fff;
  font-size: 0.62rem;
  font-weight: 700;
  padding: 0.12rem 0.5rem;
  border-radius: 5px;
  margin-left: 0.4rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  animation: glow 2s ease-in-out infinite;
}
@keyframes glow {
  0%,100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.4); }
  50% { box-shadow: 0 0 0 5px rgba(239,68,68,0); }
}
.pt { font-size: 0.97rem; font-weight: 700; color: #0f172a; margin: 0.25rem 0; line-height: 1.4; }
.pa { font-size: 0.82rem; color: #475569; margin: 0.2rem 0; line-height: 1.45; }
.pa .me {
  font-weight: 700;
  color: #1e293b;
  background: linear-gradient(135deg, #dbeafe, #ede9fe);
  padding: 0.02rem 0.3rem;
  border-radius: 3px;
}
.pl { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.5rem; }
.pl a {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.22rem 0.6rem;
  font-size: 0.7rem;
  font-weight: 600;
  border-radius: 5px;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 1px solid;
}
.pl .pdf { background: #eff6ff; color: #2563eb; border-color: #bfdbfe; }
.pl .pdf:hover { background: #2563eb; color: #fff; }
.pl .arx { background: #fef3c7; color: #d97706; border-color: #fde68a; }
.pl .arx:hover { background: #d97706; color: #fff; }
.pl .code { background: #f0fdf4; color: #16a34a; border-color: #bbf7d0; }
.pl .code:hover { background: #16a34a; color: #fff; }
.pl .proj { background: #fdf2f8; color: #db2777; border-color: #fbcfe8; }
.pl .proj:hover { background: #db2777; color: #fff; }

/* Back‑to‑top floating button */
.back-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 44px; height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  color: #fff;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(59,130,246,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 99;
  text-decoration: none;
}
.back-top.show { opacity: 1; visibility: visible; }
.back-top:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(59,130,246,0.5); color: #fff; }

.pub-footer {
  background: linear-gradient(135deg, #f8fafc, #eff6ff, #faf5ff);
  border: 2px solid #e2e8f0;
  border-radius: 14px;
  padding: 1.8rem;
  text-align: center;
  margin-top: 2.5rem;
  position: relative;
  overflow: hidden;
}
.pub-footer::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #f59e0b);
}
.fg {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.2rem;
  max-width: 450px;
  margin: 0 auto;
}
.fn {
  font-size: 2rem;
  font-weight: 900;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.fl { font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
.en { margin-top: 1rem; font-size: 0.78rem; color: #94a3b8; font-style: italic; }
</style>

<!-- ==================== HERO ==================== -->
<div class="pub-hero" id="top">
  <h1>📚 Publications</h1>
  <p class="subtitle">
    Research spanning <strong>computer vision</strong>, <strong>efficient deep learning</strong>, <strong>multi-modal models</strong>, and <strong>remote sensing</strong> — published at top-tier venues worldwide.
  </p>
  <div class="stats-grid">
    <div class="stat-card" style="cursor:default;">
      <span class="stat-number">43</span><br>
      <span class="stat-label">Total Papers</span>
    </div>
    <a href="#section-conferences" class="stat-card">
      <span class="stat-number">29</span><br>
      <span class="stat-label">Conference Papers</span>
      <div class="stat-hint">▼ click to jump</div>
    </a>
    <a href="#section-journals" class="stat-card">
      <span class="stat-number">9</span><br>
      <span class="stat-label">Journal Articles</span>
      <div class="stat-hint">▼ click to jump</div>
    </a>
    <a href="#section-preprints" class="stat-card">
      <span class="stat-number">5</span><br>
      <span class="stat-label">Preprints</span>
      <div class="stat-hint">▼ click to jump</div>
    </a>
  </div>
</div>

<!-- ==================== VENUE BADGES ==================== -->
<div class="venue-strip">
  <span class="vb vb-s">🏆 CVPR <span class="bc">3</span></span>
  <span class="vb vb-s">🏆 ICCV <span class="bc">1</span></span>
  <span class="vb vb-s">🏆 ICLR <span class="bc">2</span></span>
  <span class="vb vb-a">⭐ AAAI <span class="bc">3</span></span>
  <span class="vb vb-a">⭐ IJCAI <span class="bc">2</span></span>
  <span class="vb vb-a">⭐ KDD <span class="bc">1</span></span>
  <span class="vb vb-b">🔬 WACV <span class="bc">5</span></span>
  <span class="vb vb-b">🔬 CVPRW <span class="bc">3</span></span>
  <span class="vb vb-j">📖 IEEE TGRS</span>
  <span class="vb vb-j">📖 IEEE Sensors</span>
  <span class="vb vb-j">📖 Earth's Future</span>
</div>

<!-- ==================== QUICK NAV ==================== -->
<div class="quick-nav">
  <a href="#section-conferences" class="qn-conf">🎤 Conference Papers <span style="opacity:0.6">→ 29</span></a>
  <a href="#section-journals" class="qn-jour">📖 Journal Articles <span style="opacity:0.6">→ 9</span></a>
  <a href="#section-preprints" class="qn-pre">📝 Preprints <span style="opacity:0.6">→ 5</span></a>
</div>

<!-- ============================================================ -->
<!--                     CONFERENCE PAPERS                        -->
<!-- ============================================================ -->

<div class="section-header" id="section-conferences">
  <div class="section-icon">🎤</div>
  <h2>Peer-Reviewed Conference Papers</h2>
  <span class="pc">29 papers</span>
</div>

<!-- 2024 -->
<div class="year-div"><span class="year-pill">2024</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#1</span>
  <span class="pv pv-wacv">📷 WACV 2024</span>
  <div class="pt">A Multimodal Benchmark and Improved Architecture for Zero Shot Learning</div>
  <div class="pa">K. Doshi, A. Garg, <span class="me">B. Uzkent</span>, X. Wang, M. Omar</div>
</div>

<div class="paper"><span class="pnum">#2</span>
  <span class="pv pv-wacv">📷 WACV 2024</span>
  <div class="pt">Augment the Pairs: Semantics-Preserving Image-Caption Pair Augmentation for Grounding-Based Vision and Language Models</div>
  <div class="pa">J. Yi, <span class="me">B. Uzkent</span>, O. Ignat, Z. Li, A. Garg, X. Yu, L. Liu</div>
</div>

<!-- 2023 -->
<div class="year-div"><span class="year-pill">2023</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#3</span>
  <span class="pv pv-cvpr">🏆 CVPR 2023</span>
  <div class="pt">Dynamic Inference with Grounding Based Vision and Language Models</div>
  <div class="pa"><span class="me">B. Uzkent</span>, A. Garg, W. Zhou, K. Doshi, J. Yi, X. Wang, M. Omar</div>
</div>

<div class="paper"><span class="pnum">#4</span>
  <span class="pv pv-aaai">⭐ AAAI 2023</span>
  <div class="pt">GOHSP: A Unified Framework of Graph and Optimization-based Heterogeneous Structured Pruning for Vision Transformer</div>
  <div class="pa">M. Yin, <span class="me">B. Uzkent</span>, Y. Shen, H. Jin</div>
</div>

<div class="paper"><span class="pnum">#5</span>
  <span class="pv pv-iclr">🧠 ICLR 2023</span>
  <div class="pt">Learning to Jointly Share and Prune Weights for Grounding Based Vision and Language Models</div>
  <div class="pa">S. Gao, <span class="me">B. Uzkent</span>, Y. Shen, H. Huang, H. Jin</div>
</div>

<!-- 2022 -->
<div class="year-div"><span class="year-pill">2022</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#6</span>
  <span class="pv pv-ws">🔬 CVPRW 2022</span>
  <div class="pt">Efficient Conditional Pre-training for Transfer Learning</div>
  <div class="pa">S. Chakraborty, <span class="me">B. Uzkent</span>, K. Ayush, E. Sheehan, S. Ermon</div>
  <div class="pl"><a href="https://arxiv.org/abs/2011.10231" class="arx">📄 arXiv</a></div>
</div>

<div class="paper"><span class="pnum">#7</span>
  <span class="pv pv-cvpr">🏆 CVPR 2022</span>
  <div class="pt">Lite-MDETR: A Lightweight Multi-Modal Detector</div>
  <div class="pa">Q. Lu, Y.C. Shu, <span class="me">B. Uzkent</span>, T. Hua, Y. Shen, H. Jin</div>
</div>

<!-- 2021 -->
<div class="year-div"><span class="year-pill">2021</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#8</span>
  <span class="pv pv-iccv">🏆 ICCV 2021</span>
  <div class="pt">Geography-Aware Self-Supervised Learning</div>
  <div class="pa">K. Ayush, <span class="me">B. Uzkent</span>, C. Meng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl">
    <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Ayush_Geography-Aware_Self-Supervised_Learning_ICCV_2021_paper.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/sustainlab-group/geography-aware-ssl" class="code">💻 Code</a>
    <a href="https://geography-aware-ssl.github.io/" class="proj">🌐 Project</a>
  </div>
</div>

<div class="paper"><span class="pnum">#9</span>
  <span class="pv pv-iclr">🧠 ICLR 2021</span>
  <div class="pt">Negative Data Augmentation</div>
  <div class="pa">K. Ayush*, A. Sinha*, J. Song, <span class="me">B. Uzkent</span>, H. Jin, S. Ermon</div>
  <div class="pl">
    <a href="https://openreview.net/forum?id=Ovp8dvB8IBH" class="pdf">📄 PDF</a>
    <a href="https://github.com/ermongroup/NDA" class="code">💻 Code</a>
  </div>
</div>

<div class="paper"><span class="pnum">#10</span>
  <span class="pv pv-aaai">⭐ AAAI 2021</span>
  <div class="pt">Efficient High Resolution Image Processing using Deep Reinforcement Learning</div>
  <div class="pa"><span class="me">B. Uzkent</span>, K. Ayush, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl"><a href="https://arxiv.org/pdf/2006.04224.pdf" class="arx">📄 arXiv</a></div>
</div>

<div class="paper"><span class="pnum">#11</span>
  <span class="pv pv-aaai">⭐ AAAI 2021</span>
  <div class="pt">Predicting Geo-attributes Using Deep Learning and Publicly Available Street-level Images</div>
  <div class="pa">J. Lee, D. Grosz, <span class="me">B. Uzkent</span>, S. Zheng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/pdf/2006.08661.pdf" class="arx">📄 arXiv</a>
    <a href="https://github.com/sustainlab-group/mapillarygcn" class="code">💻 Code</a>
  </div>
</div>

<!-- 2020 -->
<div class="year-div"><span class="year-pill">2020</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#12</span>
  <span class="pv pv-ijcai">⭐ IJCAI 2020</span>
  <div class="pt">Generating Interpretable Poverty Maps Using Object Detection in Satellite Images</div>
  <div class="pa">K. Ayush, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/pdf/2002.01612.pdf" class="arx">📄 arXiv</a>
    <a href="https://www.ijcai.org/Proceedings/2020/0608.pdf" class="pdf">📄 PDF</a>
  </div>
</div>

<div class="paper"><span class="pnum">#13</span>
  <span class="pv pv-cvpr">🏆 CVPR 2020</span><span class="oral">🎯 Oral</span>
  <div class="pt">Learning When and Where to Zoom Using Deep Reinforcement Learning</div>
  <div class="pa"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/pdf/2003.00425.pdf" class="arx">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Uzkent_Learning_When_and_Where_to_Zoom_With_Deep_Reinforcement_Learning_CVPR_2020_paper.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/ermongroup/PatchDrop" class="code">💻 Code</a>
  </div>
</div>

<div class="paper"><span class="pnum">#14</span>
  <span class="pv pv-ws">🔬 CVPRW 2020</span>
  <div class="pt">Farmland Parcel Delineation using Spatio-temporal Convolutional Networks</div>
  <div class="pa">H.L. Aung, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl">
    <a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/sustainlab-group/ParcelDelineation" class="code">💻 Code</a>
  </div>
</div>

<div class="paper"><span class="pnum">#15</span>
  <span class="pv pv-wacv">📷 WACV 2020</span>
  <div class="pt">Cloud Removal from Satellite Images Using Spatiotemporal Generator Networks</div>
  <div class="pa">V. Sarukkai, A. Jain, <span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/pdf/1912.06838.pdf" class="arx">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/VSAnimator/stgan" class="code">💻 Code</a>
  </div>
</div>

<div class="paper"><span class="pnum">#16</span>
  <span class="pv pv-wacv">📷 WACV 2020</span>
  <div class="pt">Efficient Object Detection in Large Images Using Deep Reinforcement Learning</div>
  <div class="pa"><span class="me">B. Uzkent</span>, C. Yeh, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/pdf/1912.03966.pdf" class="arx">📄 arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Uzkent_Efficient_Object_Detection_in_Large_Images_Using_Deep_Reinforcement_Learning_WACV_2020_paper.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/uzkent/EfficientObjectDetection" class="code">💻 Code</a>
  </div>
</div>

<!-- 2019 -->
<div class="year-div"><span class="year-pill">2019</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#17</span>
  <span class="pv pv-ijcai">⭐ IJCAI 2019</span>
  <div class="pt">Learning How to Interpret Satellite Images using Wikipedia</div>
  <div class="pa"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, D. Lobell, M. Burke, S. Ermon</div>
  <div class="pl">
    <a href="https://arxiv.org/abs/1905.02506" class="arx">📄 arXiv</a>
    <a href="https://www.ijcai.org/proceedings/2019/0502.pdf" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/WikiSatNet" class="code">💻 Code</a>
  </div>
</div>

<div class="paper"><span class="pnum">#18</span>
  <span class="pv pv-kdd">⭐ KDD 2019</span>
  <div class="pt">Predicting Economic Development using Geolocated Wikipedia Articles</div>
  <div class="pa">E. Sheehan, C. Meng, M. Tan, <span class="me">B. Uzkent</span>, N. Jean, D. Lobell, M. Burke, S. Ermon</div>
  <div class="pl">
    <a href="https://dl.acm.org/citation.cfm?id=3330784" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/WikipediaPovertyMapping" class="code">💻 Code</a>
  </div>
</div>

<!-- 2018 -->
<div class="year-div"><span class="year-pill">2018</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#19</span>
  <span class="pv pv-wacv">📷 WACV 2018</span>
  <div class="pt">EnKCF: Ensemble of Kernelized Correlation Filters for High-Speed Object Tracking</div>
  <div class="pa"><span class="me">B. Uzkent</span>, Y. Seo</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/8354233" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/EnKCF_Tracking_WACV18" class="code">💻 Code</a>
  </div>
</div>

<!-- 2017 -->
<div class="year-div"><span class="year-pill">2017</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#20</span>
  <span class="pv pv-ws">🔬 CVPRW 2017</span>
  <div class="pt">Aerial Vehicle Tracking by Adaptive Fusion of Likelihood Maps</div>
  <div class="pa"><span class="me">B. Uzkent</span>, A. Rangnekar, M. J. Hoffman, A. Vodacek</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/8014769/" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="code">💻 Code</a>
  </div>
</div>

<!-- 2016 -->
<div class="year-div"><span class="year-pill">2016</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#21</span>
  <span class="pv pv-ws">🔬 CVPRW 2016</span>
  <div class="pt">Real-time Target Detection and Tracking in Aerial Video using Hyperspectral Features</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/7789671" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="code">💻 Code</a>
  </div>
</div>

<!-- 2015 -->
<div class="year-div"><span class="year-pill">2015</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#22</span>
  <span class="pv pv-other">ICCS 2015</span>
  <div class="pt">Spectral Validation of Measurements in a Vehicle Tracking DDDAS</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="pl"><a href="https://www.sciencedirect.com/science/article/pii/S1877050915011667" class="pdf">📄 PDF</a></div>
</div>

<div class="paper"><span class="pnum">#23</span>
  <span class="pv pv-other">SPIE 2015</span>
  <div class="pt">Background Image Understanding and Adaptive Imaging for Vehicle Tracking</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="pl"><a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9460/94600F/Background-image-understanding-and-adaptive-imaging-for-vehicle-tracking/10.1117/12.2177334.short" class="pdf">📄 PDF</a></div>
</div>

<div class="paper"><span class="pnum">#24</span>
  <span class="pv pv-other">SPIE 2015</span>
  <div class="pt">Efficient Integration of Spectral Features for Vehicle Tracking utilizing an Adaptive Sensor</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="pl"><a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9407/1/Efficient-integration-of-spectral-features-for-vehicle-tracking-utilizing-an/10.1117/12.2082266.short" class="pdf">📄 PDF</a></div>
</div>

<!-- 2014 -->
<div class="year-div"><span class="year-pill">2014</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#25</span>
  <span class="pv pv-other">IEEE WNYIPW 2014</span>
  <div class="pt">3-D MRI Cardiac Segmentation using Graph Cuts</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, E. Cherry, N. Cahill</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/6999484" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/3D_MRI_Segmentation" class="code">💻 Code</a>
  </div>
</div>

<!-- 2013 -->
<div class="year-div"><span class="year-pill">2013</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#26</span>
  <span class="pv pv-other">ICCS 2013</span>
  <div class="pt">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="pl"><a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061" class="pdf">📄 PDF</a></div>
</div>

<!-- 2011 -->
<div class="year-div"><span class="year-pill">2011</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#27</span>
  <span class="pv pv-other">IEEE ITNG 2011</span>
  <div class="pt">Pitch range-based feature extraction for audio surveillance systems</div>
  <div class="pa"><span class="me">B. Uzkent</span>, B.D. Barkana</div>
  <div class="pl"><a href="https://www.researchgate.net/profile/Buket_Barkana/publication/224245542_Pitch-Range_Based_Feature_Extraction_for_Audio_Surveillance_Systems/links/5654aa9808ae4988a7b055f7/Pitch-Range-Based-Feature-Extraction-for-Audio-Surveillance-Systems.pdf" class="pdf">📄 PDF</a></div>
</div>

<!-- 2010 -->
<div class="year-div"><span class="year-pill">2010</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#28</span>
  <span class="pv pv-other">EURO 2010</span>
  <div class="pt">Performances of the ANN, SVM, and K-means clustering methods recognizing different environmental sounds</div>
  <div class="pa">B.D. Barkana, I. Saricicek, <span class="me">B. Uzkent</span></div>
</div>

<!-- 2009 -->
<div class="year-div"><span class="year-pill">2009</span><span class="year-line"></span></div>

<div class="paper"><span class="pnum">#29</span>
  <span class="pv pv-other">METU 2009</span>
  <div class="pt">Autonomous parallel parking of non-holonomic vehicles</div>
  <div class="pa"><span class="me">B. Uzkent</span>, O. Parlaktuna</div>
</div>

<!-- ============================================================ -->
<!--                       JOURNAL PAPERS                         -->
<!-- ============================================================ -->

<div class="section-header" id="section-journals">
  <div class="section-icon">📖</div>
  <h2>Peer-Reviewed Journal Papers</h2>
  <span class="pc">9 papers</span>
</div>

<div class="paper jnl"><span class="pnum">J1</span>
  <span class="pv pv-jnl">📖 Earth's Future · 2022</span>
  <div class="pt">Safe Shelter: A Case for Prioritizing Housing Quality in Climate Adaptation Policy by Remotely Sensing Roof Tarps in the San Francisco Bay Area</div>
  <div class="pa">E. Velterop, <span class="me">B. Uzkent</span>, J. Suckale</div>
</div>

<div class="paper jnl"><span class="pnum">J2</span>
  <span class="pv pv-jnl">📖 IEEE TGRS · 2019</span>
  <div class="pt">Tracking in Aerial Hyperspectral Videos using Deep Kernelized Correlation Filters</div>
  <div class="pa"><span class="me">B. Uzkent</span>, A. Rangnekar, M.J. Hoffman</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/8435971" class="pdf">📄 PDF</a>
    <a href="https://arxiv.org/pdf/1711.07235.pdf" class="arx">📄 arXiv</a>
    <a href="https://github.com/buzkent86/HKCF_Tracker" class="code">💻 Code</a>
  </div>
</div>

<div class="paper jnl"><span class="pnum">J3</span>
  <span class="pv pv-jnl">📖 IEEE JSTARS · 2016</span>
  <div class="pt">Integrating Hyperspectral Likelihoods in a Multi-dimensional Assignment Algorithm for Aerial Vehicle Tracking</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="pl">
    <a href="https://ieeexplore.ieee.org/document/7471414" class="pdf">📄 PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code" class="code">💻 Code</a>
  </div>
</div>

<div class="paper jnl"><span class="pnum">J4</span>
  <span class="pv pv-jnl">📖 IEEE Sensors J. · 2015</span>
  <div class="pt">Feature Matching with an Adaptive Optical Sensor in a Ground Target Tracking System</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, Bin Chen</div>
  <div class="pl"><a href="https://ieeexplore.ieee.org/document/6873232/" class="pdf">📄 PDF</a></div>
</div>

<div class="paper jnl"><span class="pnum">J5</span>
  <span class="pv pv-jnl">📖 Procedia CS · 2013</span>
  <div class="pt">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="pa"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="pl"><a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061" class="pdf">📄 PDF</a></div>
</div>

<div class="paper jnl"><span class="pnum">J6</span>
  <span class="pv pv-jnl">📖 IJICIC · 2012</span>
  <div class="pt">Non-speech environmental sound classification using SVMS with a new set of features</div>
  <div class="pa"><span class="me">B. Uzkent</span>, B.D. Barkana, H. Cevikalp</div>
  <div class="pl"><a href="https://www.researchgate.net/profile/Hakan_Cevikalp/publication/267782696_Non-speech_environmental_sound_classification_using_SVMs_with_a_new_set_of_features/links/54b7bf9f0cf24eb34f6ed7ff/Non-speech-environmental-sound-classification-using-SVMs-with-a-new-set-of-features.pdf" class="pdf">📄 PDF</a></div>
</div>

<div class="paper jnl"><span class="pnum">J7</span>
  <span class="pv pv-jnl">📖 Adv. Mat. Research · 2012</span>
  <div class="pt">Normal and abnormal non-speech audio event detection using MFCC and PR-based feature sets</div>
  <div class="pa">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
</div>

<div class="paper jnl"><span class="pnum">J8</span>
  <span class="pv pv-jnl">📖 Applied Acoustics · 2011</span>
  <div class="pt">Environmental noise classifier using a new set of feature parameters based on pitch range</div>
  <div class="pa">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
  <div class="pl"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0003682X11001381" class="pdf">📄 PDF</a></div>
</div>

<div class="paper jnl"><span class="pnum">J9</span>
  <span class="pv pv-jnl">📖 Expert Syst. w/ App. · 2011</span>
  <div class="pt">Automatic environmental noise source classification model using fuzzy logic</div>
  <div class="pa"><span class="me">B. Uzkent</span>, B.D. Barkana, J. Yang</div>
  <div class="pl"><a href="https://www.sciencedirect.com/science/article/pii/S0957417411001047" class="pdf">📄 PDF</a></div>
</div>

<!-- ============================================================ -->
<!--                  PREPRINTS & TECH REPORTS                    -->
<!-- ============================================================ -->

<div class="section-header" id="section-preprints">
  <div class="section-icon">📝</div>
  <h2>Preprints &amp; Technical Reports</h2>
  <span class="pc">5 papers</span>
</div>

<div class="paper pre"><span class="pnum">P1</span>
  <span class="pv pv-pre">📝 arXiv · 2025</span>
  <div class="pt">CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models</div>
  <div class="pa">T. Poppi, <span class="me">B. Uzkent</span>, A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, R. Cucchiara, F. Schiffers</div>
  <div class="pl"><a href="https://arxiv.org/abs/2601.04778" class="arx">📄 arXiv</a></div>
</div>

<div class="paper pre"><span class="pnum">P2</span>
  <span class="pv pv-pre">📝 arXiv · 2025</span>
  <div class="pt">From Frames to Clips: Efficient Key Clip Selection for Long-Form Video Understanding</div>
  <div class="pa">G. Sun, A. Singhal, <span class="me">B. Uzkent</span>, M. Shah, C. Chen, G. Kessler</div>
  <div class="pl">
    <a href="https://arxiv.org/abs/2510.02262" class="arx">📄 arXiv</a>
    <a href="https://guangyusun.com/f2c/" class="proj">🌐 Project</a>
  </div>
</div>

<div class="paper pre"><span class="pnum">P3</span>
  <span class="pv pv-pre">📝 Preprint</span>
  <div class="pt">Domain Adaptation Using Adversarial Learning for Studying Low Resolution Images</div>
  <div class="pa"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="pl"><a href="https://www.researchgate.net/publication/341030568_Adversarial_Domain_Adaptation_for_Analyzing_Low_Resolution_Images" class="arx">📄 ResearchGate</a></div>
</div>

<div class="paper pre"><span class="pnum">P4</span>
  <span class="pv pv-pre">📝 arXiv</span>
  <div class="pt">Learning to Interpret Satellite Images in Global Scale Using Wikipedia</div>
  <div class="pa"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl"><a href="https://arxiv.org/pdf/1905.02506.pdf" class="arx">📄 arXiv</a></div>
</div>

<div class="paper pre"><span class="pnum">P5</span>
  <span class="pv pv-pre">📝 arXiv</span>
  <div class="pt">Learning to interpret satellite images using wikipedia</div>
  <div class="pa">E. Sheehan, <span class="me">B. Uzkent</span>, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="pl"><a href="https://arxiv.org/pdf/1809.10236.pdf" class="arx">📄 arXiv</a></div>
</div>

<!-- ==================== FOOTER ==================== -->

<div class="pub-footer">
  <div class="fg">
    <div><div class="fn">9</div><div class="fl">Journal Papers</div></div>
    <div><div class="fn">29</div><div class="fl">Conference Papers</div></div>
    <div><div class="fn">5</div><div class="fl">Preprints</div></div>
  </div>
  <p class="en">* denotes equal contribution</p>
</div>

<!-- Back to top button -->
<a href="#top" class="back-top" id="backTop" title="Back to top">⬆</a>

<script>
// Show/hide back-to-top button on scroll
window.addEventListener('scroll', function() {
  var btn = document.getElementById('backTop');
  if (window.scrollY > 400) {
    btn.classList.add('show');
  } else {
    btn.classList.remove('show');
  }
});

// Smooth scroll for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    var target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
</script>
```

**What changed to add clickable navigation:**

1. **Hero stat cards are now `<a>` links** — the Conference (29), Journal (9), and Preprints (5) cards in the hero section link to `#section-conferences`, `#section-journals`, and `#section-preprints` with a small "▼ click to jump" hint

2. **Quick-nav bar** added below the venue badges — three prominent styled buttons that jump to each section

3. **Section `id` anchors** — each `section-header` div has `id="section-conferences"`, `id="section-journals"`, `id="section-preprints"` and `scroll-margin-top: 80px` so they don't hide behind a sticky navbar

4. **Smooth scrolling** via a small `<script>` block that intercepts all `#` anchor clicks

5. **Back-to-top button** — a floating ⬆ button that appears after scrolling down 400px, linking back to `#top`
