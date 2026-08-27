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
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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
.theme-card > p {
  margin: 0 0 0.65rem 0;
  font-size: 0.9rem;
  color: #444;
  line-height: 1.55;
}
.theme-papers {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.84rem;
  color: #374151;
  line-height: 1.5;
}
.theme-papers li { margin-bottom: 0.35rem; }
.theme-papers a {
  color: #2563eb;
  font-weight: 600;
  text-decoration: none;
}
.theme-papers a:hover { text-decoration: underline; }
.theme-papers .venue {
  color: #6b7280;
  font-weight: 500;
}

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
    <ul class="theme-papers">
      <li><a href="https://arxiv.org/pdf/2510.02262">From Frames to Clips</a> <span class="venue">· ECCV 2026 Workshop (Accepted)</span></li>
      <li><a href="https://arxiv.org/pdf/2603.25145">Learning to Rank Caption Chains</a> <span class="venue">· arXiv</span></li>
      <li><a href="https://arxiv.org/pdf/2601.04778">CounterVid</a> <span class="venue">· EMNLP 2026 (Accepted)</span></li>
      <li><a href="https://arxiv.org/pdf/2603.19481">Narrative Aligned Long Form Video QA</a> <span class="venue">· CVPR Workshop 2026</span></li>
    </ul>
  </div>

  <div class="theme-card">
    <h2>⚡ Efficient &amp; Multimodal Models</h2>
    <p>Dynamic inference, structured pruning, weight sharing, and lightweight detectors for grounding-based vision-and-language models.</p>
    <ul class="theme-papers">
      <li><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Uzkent_Dynamic_Inference_With_Grounding_Based_Vision_and_Language_Models_CVPR_2023_paper.pdf">Dynamic Inference with Grounding Based V&amp;L Models</a> <span class="venue">· CVPR 2023</span></li>
      <li><a href="https://arxiv.org/pdf/2301.05345.pdf">GOHSP: Graph &amp; Optimization-based Structured Pruning</a> <span class="venue">· AAAI 2023</span></li>
      <li><a href="https://openreview.net/pdf?id=UMERaIHMwB3">Learning to Jointly Share and Prune Weights</a> <span class="venue">· ICLR 2023</span></li>
      <li><a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Lou_Lite-MDETR_A_Lightweight_Multi-Modal_Detector_CVPR_2022_paper.pdf">Lite-MDETR</a> <span class="venue">· CVPR 2022</span></li>
      <li><a href="https://openaccess.thecvf.com/content/CVPR2022W/L3D-IVU/papers/Chakraborty_Efficient_Conditional_Pre-Training_for_Transfer_Learning_CVPRW_2022_paper.pdf">Efficient Conditional Pre-training for Transfer Learning</a> <span class="venue">· CVPR Workshop 2022</span></li>
      <li><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Yi_Augment_the_Pairs_Semantics-Preserving_Image-Caption_Pair_Augmentation_for_Grounding-Based_Vision_WACV_2024_paper.pdf">Augment the Pairs</a> <span class="venue">· WACV 2024</span></li>
      <li><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Doshi_A_Multimodal_Benchmark_and_Improved_Architecture_for_Zero_Shot_Learning_WACV_2024_paper.pdf">Multimodal Benchmark for Zero-Shot Learning</a> <span class="venue">· WACV 2024</span></li>
      <li><a href="https://arxiv.org/pdf/2006.04224.pdf">Efficient High Resolution Image Processing with Deep RL</a> <span class="venue">· AAAI 2021</span></li>
    </ul>
  </div>

  <div class="theme-card">
    <h2>🌱 Computational Sustainability</h2>
    <p>Remote sensing, geolocated data, self-supervised learning, and interpretable models for agriculture, poverty mapping, and environmental monitoring.</p>
    <ul class="theme-papers">
      <li><a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Ayush_Geography-Aware_Self-Supervised_Learning_ICCV_2021_paper.pdf">Geography-Aware Self-Supervised Learning</a> <span class="venue">· ICCV 2021</span></li>
      <li><a href="https://www.ijcai.org/Proceedings/2020/0608.pdf">Learning How to Interpret Satellite Images using Wikipedia</a> <span class="venue">· IJCAI 2020</span></li>
      <li><a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Uzkent_Learning_When_and_Where_to_Zoom_With_Deep_Reinforcement_Learning_CVPR_2020_paper.pdf">Learning When and Where to Zoom</a> <span class="venue">· CVPR 2020 (Oral)</span></li>
      <li><a href="https://arxiv.org/pdf/2006.08661.pdf">Predicting Geo-attributes with Street-Level Images</a> <span class="venue">· AAAI 2021</span></li>
      <li><a href="https://dl.acm.org/doi/10.1145/3292500.3330784">Predicting Economic Development using Geolocated Wikipedia</a> <span class="venue">· KDD 2019</span></li>
      <li><a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf">Farmland Parcel Delineation</a> <span class="venue">· CVPR Workshop 2020</span></li>
      <li><a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf">Cloud Removal from Satellite Images</a> <span class="venue">· WACV 2020</span></li>
      <li><a href="/datasets/">Open datasets</a> <span class="venue">· MapillaryGCN, cloud removal, WAMI</span></li>
    </ul>
  </div>

  <div class="theme-card">
    <h2>🎨 Generative Models</h2>
    <p>Generative modeling for satellite imagery, data augmentation, and counterfactual video generation for robust VLM evaluation.</p>
    <ul class="theme-papers">
      <li><a href="https://arxiv.org/pdf/2601.04778">CounterVid: Counterfactual Video Generation</a> <span class="venue">· EMNLP 2026 (Accepted)</span></li>
      <li><a href="https://openreview.net/forum?id=Ovp8dvB8IBH">Negative Data Augmentation</a> <span class="venue">· ICLR 2021</span></li>
      <li><a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf">Cloud Removal (Spatiotemporal GAN)</a> <span class="venue">· WACV 2020</span></li>
      <li><a href="https://github.com/VSAnimator/stgan">Cloud removal code</a> <span class="venue">· GitHub</span></li>
    </ul>
  </div>

</div>

<p style="font-size:0.9rem;color:#6b7280;">
  See the full <a href="/publications/">publication list</a> or <a href="https://scholar.google.com/citations?user=-Es6xrgAAAAJ&amp;hl=en">Google Scholar</a> profile for a complete bibliography.
</p>
