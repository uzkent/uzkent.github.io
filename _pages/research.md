---
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

<style>
.research-header { margin-bottom: 1.5rem; }
.research-header h1 { font-size: 1.8rem; margin: 0 0 0.3rem 0; color: #1a1a1a; }
.research-header-line { width: 120px; height: 3px; background: #2563eb; border-radius: 2px; }
.research-header p { color: #6b7280; font-size: 0.92rem; margin: 0.5rem 0 0; line-height: 1.5; }

.theme-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.1rem;
  margin: 1.5rem 0 2rem;
}
.theme-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-top: 4px solid #2563eb;
  border-radius: 10px;
  padding: 1.2rem 1.3rem;
}
.theme-card h2 {
  font-size: 1.05rem;
  margin: 0 0 0.5rem 0;
  color: #1a1a1a;
}
.theme-card p {
  margin: 0;
  font-size: 0.9rem;
  color: #444;
  line-height: 1.55;
}
.theme-links {
  margin-top: 0.65rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.theme-links a {
  font-size: 0.8rem;
  font-weight: 600;
  color: #2563eb;
  text-decoration: none;
}
.theme-links a:hover { text-decoration: underline; }

.hiring-banner {
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  padding: 0.85rem 1.1rem;
  margin: 0 0 1.5rem 0;
  font-size: 0.92rem;
  color: #1e3a5f;
  line-height: 1.5;
}
</style>

<div class="research-header">
  <h1>🔬 Research</h1>
  <div class="research-header-line"></div>
  <p>Generative AI, video-language understanding, efficient deep learning, and machine learning for sustainability.</p>
</div>

<div class="hiring-banner">
  <strong>Hiring at AMD:</strong> We are hiring for full-time positions at all levels working on generative AI applications on AMD hardware.
</div>

<div class="theme-grid">

  <div class="theme-card">
    <h2>🎥 Video-Language &amp; Long-Form Video</h2>
    <p>Foundational models and systems for long-form video understanding, captioning, ranking, and mitigating hallucinations in video-language models.</p>
    <div class="theme-links">
      <a href="/publications/">Publications</a>
      <a href="https://arxiv.org/pdf/2510.02262">F2C (arXiv)</a>
    </div>
  </div>

  <div class="theme-card">
    <h2>⚡ Efficient &amp; Multimodal Models</h2>
    <p>Dynamic inference, structured pruning, weight sharing, and lightweight detectors for grounding-based vision-and-language models.</p>
    <div class="theme-links">
      <a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Uzkent_Dynamic_Inference_With_Grounding_Based_Vision_and_Language_Models_CVPR_2023_paper.pdf">CVPR 2023 PDF</a>
      <a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Lou_Lite-MDETR_A_Lightweight_Multi-Modal_Detector_CVPR_2022_paper.pdf">Lite-MDETR</a>
    </div>
  </div>

  <div class="theme-card">
    <h2>🌱 Computational Sustainability</h2>
    <p>Remote sensing, geolocated data, self-supervised learning, and interpretable models for agriculture, poverty mapping, and environmental monitoring.</p>
    <div class="theme-links">
      <a href="/datasets/">Datasets</a>
      <a href="https://geography-aware-ssl.github.io/">Geography-Aware SSL</a>
      <a href="https://github.com/sustainlab-group/mapillarygcn">MapillaryGCN</a>
    </div>
  </div>

  <div class="theme-card">
    <h2>🎨 Generative Models</h2>
    <p>Generative modeling for satellite imagery (cloud removal), data augmentation, and counterfactual video generation for robust VLM evaluation.</p>
    <div class="theme-links">
      <a href="https://github.com/VSAnimator/stgan">Cloud removal code</a>
      <a href="https://arxiv.org/pdf/2601.04778">CounterVid</a>
    </div>
  </div>

</div>

<p style="font-size:0.9rem;color:#6b7280;">
  See the full <a href="/publications/">publication list</a> or <a href="https://scholar.google.com/citations?user=-Es6xrgAAAAJ&amp;hl=en">Google Scholar</a> profile for a complete bibliography.
</p>
