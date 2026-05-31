---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
  /* ── palette & tokens ── */
  :root {
    --accent: #0073e6;
    --accent-light: #e8f2fc;
    --bg-card: #fafbfd;
    --border: #e2e6ea;
    --shadow: 0 2px 8px rgba(0,0,0,.06);
    --radius: 10px;
  }

  /* ── section titles ── */
  .section-title {
    display: inline-block;
    font-size: 1.55rem;
    font-weight: 700;
    letter-spacing: .3px;
    margin: 2.2rem 0 .9rem;
    padding-bottom: .35rem;
    border-bottom: 3px solid var(--accent);
  }

  /* ── hero card ── */
  .hero-card {
    background: linear-gradient(135deg, var(--accent-light) 0%, #f4f7fb 100%);
    border-left: 5px solid var(--accent);
    border-radius: var(--radius);
    padding: 1.6rem 1.8rem;
    margin: 1rem 0 2rem;
    box-shadow: var(--shadow);
    line-height: 1.75;
  }
  .hero-card p { margin: .55rem 0; }

  /* ── timeline ── */
  .timeline { position: relative; padding-left: 28px; margin: .6rem 0 2rem; }
  .timeline::before {
    content: '';
    position: absolute;
    left: 7px; top: 0; bottom: 0;
    width: 3px;
    background: var(--accent);
    border-radius: 3px;
  }
  .timeline-item {
    position: relative;
    display: flex;
    align-items: flex-start;
    gap: 1.1rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.1rem 1.4rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow);
    transition: transform .2s, box-shadow .2s;
  }
  .timeline-logo {
    width: 52px;
    height: 52px;
    object-fit: contain;
    flex-shrink: 0;
    padding: 6px;
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-top: 0.1rem;
  }
  .timeline-content {
    flex: 1;
    min-width: 0;
  }
  .timeline-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(0,0,0,.1);
  }
  .timeline-item::before {
    content: '';
    position: absolute;
    left: -24px; top: 1.35rem;
    width: 13px; height: 13px;
    background: var(--accent);
    border: 3px solid #fff;
    border-radius: 50%;
    box-shadow: 0 0 0 2px var(--accent);
  }
  .timeline-role {
    font-weight: 700;
    font-size: 1.05rem;
    color: #1a1a1a;
  }
  .timeline-org {
    color: var(--accent);
    font-weight: 600;
  }
  .timeline-date {
    float: right;
    font-size: .85rem;
    color: #777;
    font-style: italic;
  }
  .timeline-desc {
    margin-top: .4rem;
    font-size: .93rem;
    color: #444;
  }

  /* ── education cards ── */
  .edu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.1rem;
    margin: .6rem 0 2rem;
  }
  .edu-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-top: 4px solid var(--accent);
    border-radius: var(--radius);
    padding: 1.3rem 1.4rem;
    box-shadow: var(--shadow);
    transition: transform .2s, box-shadow .2s;
  }
  .edu-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(0,0,0,.1);
  }
  .edu-degree {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--accent);
  }
  .edu-inst { font-weight: 600; margin: .25rem 0; }
  .edu-years { font-size: .85rem; color: #777; }
  .edu-focus {
    margin-top: .5rem;
    font-size: .9rem;
    color: #444;
    border-left: 3px solid var(--accent-light);
    padding-left: .65rem;
  }

  /* ── interest pills ── */
  .interest-grid {
    display: flex;
    flex-wrap: wrap;
    gap: .7rem;
    margin: .6rem 0 2rem;
  }
  .interest-pill {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    background: var(--accent-light);
    color: #0059b3;
    font-weight: 600;
    font-size: .92rem;
    padding: .55rem 1.15rem;
    border-radius: 50px;
    border: 1px solid #c9ddf4;
    transition: background .2s, transform .15s;
    cursor: default;
  }
  .interest-pill:hover {
    background: #d1e4f9;
    transform: scale(1.04);
  }
</style>

<!-- ════════════════════════════════════════════════════ -->

<span class="section-title">&ensp;About Me</span>

<div class="hero-card">
  <p>
    I am a <strong>Principal Member of Staff</strong> at <strong>AMD</strong>, where I work on the applications of <strong>Generative AI</strong> on <strong>AMD hardware</strong> since April 2026.
  </p>
  <p>
    Previously, I was a <strong>Machine Learning Scientist</strong> at <strong>Amazon Prime Video</strong>, where I developed <em>Video-Language Foundational Models</em> that bridge visual and linguistic understanding at scale.
  </p>
  <p>
    Previously, I was a <strong>Postdoctoral Research Fellow</strong> at the
    <a href="http://ai.stanford.edu" target="_blank">Stanford AI Lab</a> (Stanford University),
    working under the guidance of
    <a href="https://cs.stanford.edu/~ermon/" target="_blank">Dr.&nbsp;Stefano Ermon</a>.
    I am deeply grateful to Dr.&nbsp;Ermon for his exceptional mentorship and support.
  </p>
  <p>
    My research at Stanford spanned <strong>efficient convolutional networks</strong> optimized for run-time complexity, <strong>unsupervised &amp; weakly supervised learning</strong> for improved sample efficiency, <strong>generative models</strong>, and <strong>machine learning for computational sustainability</strong>.
  </p>
  <p>
    I earned my Ph.D. from the
    <a href="https://www.cis.rit.edu" target="_blank">Chester F. Carlson Center for Imaging Science</a>
    at Rochester Institute of Technology, advised by
    <a href="https://people.rit.edu/mjhsma/index.html" target="_blank">Dr.&nbsp;Matthew J. Hoffman</a>.
  </p>
</div>

<!-- ════════════════════════════════════════════════════ -->

<span class="section-title">🎓&ensp;Education</span>

<div class="edu-grid">

  <div class="edu-card">
    <div class="edu-degree">Ph.D.</div>
    <div class="edu-inst">Chester F. Carlson Center for Imaging Science, RIT</div>
    <div class="edu-years">2011 – 2016</div>
    <div class="edu-focus"><em>Aerial Vehicle Detection and Tracking using a Multi-modal Adaptive Sensor</em></div>
  </div>

  <div class="edu-card">
    <div class="edu-degree">M.S.</div>
    <div class="edu-inst">Electrical &amp; Computer Engineering, University of Bridgeport</div>
    <div class="edu-years">2009 – 2011</div>
    <div class="edu-focus"><em>Non-speech Environmental Sound Classification with Pitch Range-based Features</em></div>
  </div>

  <div class="edu-card">
    <div class="edu-degree">B.S.</div>
    <div class="edu-inst">Electrical &amp; Electronics Engineering, Eskişehir Osmangazi University</div>
    <div class="edu-years">2004 – 2009</div>
    <div class="edu-focus"><em>Autonomous Parallel Parking of Non-holonomic Vehicles</em></div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════ -->

<span class="section-title">💼&ensp;Professional Experience</span>

<div class="timeline">

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/amd.svg" alt="AMD logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Apr 2026 – Present</span>
      <div class="timeline-role">Principal Member of Staff</div>
      <div class="timeline-org">AMD</div>
      <div class="timeline-desc">Applications of Generative AI on AMD hardware</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/amazon.svg" alt="Amazon logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Apr 2022 – Mar 2026</span>
      <div class="timeline-role">Machine Learning Scientist</div>
      <div class="timeline-org">Amazon Prime Video</div>
      <div class="timeline-desc">Video-Language Foundational Models</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/samsung.svg" alt="Samsung logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Nov 2020 – Apr 2022</span>
      <div class="timeline-role">Sr. Research Scientist</div>
      <div class="timeline-org">Samsung Research America</div>
      <div class="timeline-desc">Vision Transformer Compression · Multimodal Understanding</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/stanford.png" alt="Stanford University logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Jul 2018 – Oct 2020</span>
      <div class="timeline-role">Postdoctoral Research Fellow</div>
      <div class="timeline-org">Stanford University — Stanford AI Lab</div>
      <div class="timeline-desc">Self-Supervised Learning · Dynamic Models · Generative Models · Computational Sustainability</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/planet.png" alt="Planet Labs logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Jun 2017 – Jul 2018</span>
      <div class="timeline-role">Computer Vision Engineer</div>
      <div class="timeline-org">Planet Labs</div>
      <div class="timeline-desc">Convolutional Object Detection in Low-Resolution Aerial Imagery</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/autel.png" alt="Autel Robotics logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Aug 2016 – Jun 2017</span>
      <div class="timeline-role">Computer Vision Engineer</div>
      <div class="timeline-org">Autel Robotics</div>
      <div class="timeline-desc">High-Speed Object Tracking on Low-End Embedded Systems</div>
    </div>
  </div>

  <div class="timeline-item">
    <img class="timeline-logo" src="/images/logos/huawei.svg" alt="Huawei logo" width="52" height="52" loading="lazy">
    <div class="timeline-content">
      <span class="timeline-date">Nov 2015 – May 2016</span>
      <div class="timeline-role">Computer Vision Algorithm Engineer Intern</div>
      <div class="timeline-org">Huawei R&amp;D</div>
      <div class="timeline-desc">Unsupervised Semantic Role Assignment in Photo Albums</div>
    </div>
  </div>

</div>

<!-- ════════════════════════════════════════════════════ -->

<span class="section-title">🔬&ensp;Research Interests</span>

<div class="interest-grid">
  <span class="interest-pill">🎥 Video-Language Understanding</span>
  <span class="interest-pill">⚡ Efficient Deep Learning &amp; Model Compression</span>
  <span class="interest-pill">🤖 Multimodal Machine Learning</span>
  <span class="interest-pill">🌱 Computational Sustainability</span>
  <span class="interest-pill">🎨 Generative Models</span>
</div>
