---
title: ""
permalink: /publications/
author_profile: true
redirect_from:
  - /publications
---

{% include base_path %}

<style>
.pub-header {
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
}
.pub-header h1 { font-size: 1.8rem; margin: 0 0 0.3rem 0; color: #1a1a1a; }
.pub-header-line { width: 120px; height: 3px; background: #2563eb; border-radius: 2px; margin-bottom: 0.5rem; }
.pub-header p { color: #6b7280; font-size: 0.92rem; margin: 0; line-height: 1.5; }

.pub-nav {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.pub-nav a {
  color: #2563eb;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
}
.pub-nav a:hover { text-decoration: underline; }

/* Section headers */
.section-title {
  font-size: 1.4rem;
  color: #1a1a1a;
  margin: 2.5rem 0 0.3rem 0;
  scroll-margin-top: 80px;
}
.section-title .icon { margin-right: 0.4rem; }
.section-line { width: 100px; height: 3px; background: #2563eb; border-radius: 2px; margin-bottom: 1.5rem; }
.section-count {
  font-size: 0.85rem;
  color: #9ca3af;
  font-weight: 400;
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 28px;
  margin-left: 8px;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 0;
  bottom: 0;
  width: 3px;
  background: #2563eb;
  border-radius: 2px;
}

/* Year markers */
.year-marker {
  position: relative;
  margin: 1.8rem 0 0.8rem 0;
}
.year-marker::before {
  content: '';
  position: absolute;
  left: -28px;
  top: 50%;
  transform: translateY(-50%);
  width: 17px;
  height: 17px;
  background: #fff;
  border: 3px solid #2563eb;
  border-radius: 50%;
  z-index: 1;
}
.year-marker span {
  font-size: 1rem;
  font-weight: 800;
  color: #1a1a1a;
}

/* Paper entries */
.paper {
  position: relative;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1rem 1.2rem;
  margin-bottom: 0.7rem;
}
.paper::before {
  content: '';
  position: absolute;
  left: -24px;
  top: 1.2rem;
  width: 9px;
  height: 9px;
  background: #fff;
  border: 2.5px solid #2563eb;
  border-radius: 50%;
  z-index: 1;
}

.paper-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}
.paper-venue {
  font-size: 0.78rem;
  font-weight: 700;
  color: #2563eb;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.paper-venue .oral-tag {
  color: #dc2626;
  font-weight: 700;
}
.paper-venue .best-paper-tag {
  color: #d97706;
  font-weight: 700;
}
.paper-venue .under-review-tag {
  color: #6b7280;
  font-weight: 600;
  font-style: italic;
}
.paper-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #111827;
  margin: 0.25rem 0;
  line-height: 1.4;
}
.paper-authors {
  font-size: 0.83rem;
  color: #6b7280;
  line-height: 1.45;
}
.paper-authors .me {
  font-weight: 700;
  color: #2563eb;
}
.paper-links {
  display: flex;
  gap: 0.7rem;
  margin-top: 0.4rem;
  flex-wrap: wrap;
}
.paper-links a {
  font-size: 0.76rem;
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}
.paper-links a:hover { text-decoration: underline; }

/* Google Scholar metrics */
.scholar-metrics {
  margin: 0 0 2.5rem 0;
  padding: 1.25rem 1.35rem 1.1rem;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}
.scholar-metrics-title {
  font-size: 1.35rem;
  margin: 0 0 0.35rem 0;
  color: #1a1a1a;
}
.scholar-metrics-line {
  width: 100px;
  height: 3px;
  background: #2563eb;
  border-radius: 2px;
  margin-bottom: 1rem;
}
.scholar-metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1rem;
}
.scholar-stat {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 0.65rem 0.85rem;
  text-align: center;
}
.scholar-stat-value {
  font-size: 1.45rem;
  font-weight: 800;
  color: #2563eb;
  line-height: 1.2;
}
.scholar-stat-label {
  font-size: 0.78rem;
  color: #6b7280;
  margin-top: 0.15rem;
}
.scholar-chart-wrap {
  position: relative;
  height: 320px;
  max-width: 100%;
}
.scholar-metrics-foot {
  margin: 0.75rem 0 0;
  font-size: 0.8rem;
  color: #6b7280;
}
.scholar-metrics-foot a { color: #2563eb; font-weight: 600; }
</style>

<div class="pub-header">
  <h1>📚 Publications</h1>
  <div class="pub-header-line"></div>
  <p>Research in computer vision, efficient deep learning, multi-modal models, and remote sensing.</p>
</div>

<div class="pub-nav">
  <a href="#scholar-metrics-title">📈 Citations</a>
  <a href="#conferences">🎤 Conference Papers (33)</a>
  <a href="#journals">📖 Journal Articles (9)</a>
  <a href="#preprints">📝 Preprints (2)</a>
</div>

{% include scholar-citations-chart.html %}

<!-- ============================================================ -->
<!--                     CONFERENCE PAPERS                        -->
<!-- ============================================================ -->

<h2 class="section-title" id="conferences"><span class="icon">🎤</span> Conference Papers <span class="section-count">(33)</span></h2>
<div class="section-line"></div>

<div class="timeline">

<div class="year-marker"><span>2026</span></div>

<div class="paper">
  <div class="paper-venue">EMNLP 2026 · <span class="under-review-tag">Under Review</span></div>
  <div class="paper-title">CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models</div>
  <div class="paper-authors">T. Poppi, <span class="me">B. Uzkent</span>, A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, R. Cucchiara, F. Schiffers</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/2601.04778">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">ECCV 2026 · <span class="under-review-tag">Under Review</span></div>
  <div class="paper-title">From Frames to Clips: Efficient Key Clip Selection for Long-Form Video Understanding</div>
  <div class="paper-authors">G. Sun, A. Singhal, <span class="me">B. Uzkent</span>, M. Shah, C. Chen, G. Kessler</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2510.02262">arXiv</a>
    <a href="https://guangyusun.com/f2c/">Project</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">ECCV 2026 · <span class="under-review-tag">Under Review</span></div>
  <div class="paper-title">Learning to Rank Caption Chains for Video-Text Alignment</div>
  <div class="paper-authors">A. Blume, <span class="me">B. Uzkent</span>, S. Chaudhuri, G. Kessler</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/2603.25145">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2026 · <span class="best-paper-tag">Best Paper Candidate</span></div>
  <div class="paper-title">Narrative Aligned Long Form Video Question Answering</div>
  <div class="paper-authors">R. Jain, K. Doshi, <span class="me">B. Uzkent</span>, G. Kessler</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/2603.19481">arXiv</a></div>
</div>

<div class="year-marker"><span>2024</span></div>

<div class="paper">
  <div class="paper-venue">WACV 2024</div>
  <div class="paper-title">A Multimodal Benchmark and Improved Architecture for Zero Shot Learning</div>
  <div class="paper-authors">K. Doshi, A. Garg, <span class="me">B. Uzkent</span>, X. Wang, M. Omar</div>
  <div class="paper-links"><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Doshi_A_Multimodal_Benchmark_and_Improved_Architecture_for_Zero_Shot_Learning_WACV_2024_paper.pdf">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">WACV 2024</div>
  <div class="paper-title">Augment the Pairs: Semantics-Preserving Image-Caption Pair Augmentation for Grounding-Based Vision and Language Models</div>
  <div class="paper-authors">J. Yi, <span class="me">B. Uzkent</span>, O. Ignat, Z. Li, A. Garg, X. Yu, L. Liu</div>
  <div class="paper-links"><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Yi_Augment_the_Pairs_Semantics-Preserving_Image-Caption_Pair_Augmentation_for_Grounding-Based_Vision_WACV_2024_paper.pdf">PDF</a></div>
</div>

<div class="year-marker"><span>2023</span></div>

<div class="paper">
  <div class="paper-venue">CVPR 2023</div>
  <div class="paper-title">Dynamic Inference with Grounding Based Vision and Language Models</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Garg, W. Zhou, K. Doshi, J. Yi, X. Wang, M. Omar</div>
  <div class="paper-links"><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Uzkent_Dynamic_Inference_With_Grounding_Based_Vision_and_Language_Models_CVPR_2023_paper.pdf">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">AAAI 2023</div>
  <div class="paper-title">GOHSP: A Unified Framework of Graph and Optimization-based Heterogeneous Structured Pruning for Vision Transformer</div>
  <div class="paper-authors">M. Yin, <span class="me">B. Uzkent</span>, Y. Shen, H. Jin</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/2301.05345.pdf">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">ICLR 2023</div>
  <div class="paper-title">Learning to Jointly Share and Prune Weights for Grounding Based Vision and Language Models</div>
  <div class="paper-authors">S. Gao, <span class="me">B. Uzkent</span>, Y. Shen, H. Huang, H. Jin</div>
  <div class="paper-links"><a href="https://openreview.net/pdf?id=UMERaIHMwB3">PDF</a></div>
</div>

<div class="year-marker"><span>2022</span></div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2022</div>
  <div class="paper-title">Efficient Conditional Pre-training for Transfer Learning</div>
  <div class="paper-authors">S. Chakraborty, <span class="me">B. Uzkent</span>, K. Ayush, E. Sheehan, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content/CVPR2022W/L3D-IVU/papers/Chakraborty_Efficient_Conditional_Pre-Training_for_Transfer_Learning_CVPRW_2022_paper.pdf">PDF</a>
    <a href="https://arxiv.org/abs/2011.10231">arXiv</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR 2022</div>
  <div class="paper-title">Lite-MDETR: A Lightweight Multi-Modal Detector</div>
  <div class="paper-authors">Q. Lu, Y.C. Shu, <span class="me">B. Uzkent</span>, T. Hua, Y. Shen, H. Jin</div>
  <div class="paper-links"><a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Lou_Lite-MDETR_A_Lightweight_Multi-Modal_Detector_CVPR_2022_paper.pdf">PDF</a></div>
</div>

<div class="year-marker"><span>2021</span></div>

<div class="paper">
  <div class="paper-venue">ICCV 2021</div>
  <div class="paper-title">Geography-Aware Self-Supervised Learning</div>
  <div class="paper-authors">K. Ayush, <span class="me">B. Uzkent</span>, C. Meng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Ayush_Geography-Aware_Self-Supervised_Learning_ICCV_2021_paper.pdf">PDF</a>
    <a href="https://github.com/sustainlab-group/geography-aware-ssl">Code</a>
    <a href="https://geography-aware-ssl.github.io/">Project</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">ICLR 2021</div>
  <div class="paper-title">Negative Data Augmentation</div>
  <div class="paper-authors">K. Ayush*, A. Sinha*, J. Song, <span class="me">B. Uzkent</span>, H. Jin, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openreview.net/forum?id=Ovp8dvB8IBH">PDF</a>
    <a href="https://github.com/ermongroup/NDA">Code</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">AAAI 2021</div>
  <div class="paper-title">Efficient High Resolution Image Processing using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, K. Ayush, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2006.04224.pdf">arXiv</a>
    <a href="https://www.aaai.org/AAAI21Papers/AAAI-10300.AyushK.pdf">PDF</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">AAAI 2021</div>
  <div class="paper-title">Predicting Geo-attributes Using Deep Learning and Publicly Available Street-level Images</div>
  <div class="paper-authors">J. Lee, D. Grosz, <span class="me">B. Uzkent</span>, S. Zheng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2006.08661.pdf">arXiv</a>
    <a href="https://github.com/sustainlab-group/mapillarygcn">Code</a>
    <a href="https://www.aaai.org/AAAI21Papers/AAAI-10056.LeeJ.pdf">PDF</a>
  </div>
</div>

<div class="year-marker"><span>2020</span></div>

<div class="paper">
  <div class="paper-venue">IJCAI 2020</div>
  <div class="paper-title">Generating Interpretable Poverty Maps Using Object Detection in Satellite Images</div>
  <div class="paper-authors">K. Ayush, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2002.01612.pdf">arXiv</a>
    <a href="https://www.ijcai.org/Proceedings/2020/0608.pdf">PDF</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR 2020 · <span class="oral-tag">Oral</span></div>
  <div class="paper-title">Learning When and Where to Zoom Using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2003.00425.pdf">arXiv</a>
    <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Uzkent_Learning_When_and_Where_to_Zoom_With_Deep_Reinforcement_Learning_CVPR_2020_paper.pdf">PDF</a>
    <a href="https://github.com/ermongroup/PatchDrop">Code</a>
    <a href="https://www.youtube.com/watch?v=n0HGh2x6Cgg">Video</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2020</div>
  <div class="paper-title">Farmland Parcel Delineation using Spatio-temporal Convolutional Networks</div>
  <div class="paper-authors">H.L. Aung, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf">PDF</a>
    <a href="https://arxiv.org/pdf/2004.05471.pdf">arXiv</a>
    <a href="https://github.com/sustainlab-group/ParcelDelineation">Code</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">WACV 2020</div>
  <div class="paper-title">Cloud Removal from Satellite Images Using Spatiotemporal Generator Networks</div>
  <div class="paper-authors">V. Sarukkai, A. Jain, <span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1912.06838.pdf">arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf">PDF</a>
    <a href="https://github.com/VSAnimator/stgan">Code</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">WACV 2020</div>
  <div class="paper-title">Efficient Object Detection in Large Images Using Deep Reinforcement Learning</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, C. Yeh, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1912.03966.pdf">arXiv</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Uzkent_Efficient_Object_Detection_in_Large_Images_Using_Deep_Reinforcement_Learning_WACV_2020_paper.pdf">PDF</a>
    <a href="https://github.com/uzkent/EfficientObjectDetection">Code</a>
  </div>
</div>

<div class="year-marker"><span>2019</span></div>

<div class="paper">
  <div class="paper-venue">IJCAI 2019</div>
  <div class="paper-title">Learning How to Interpret Satellite Images using Wikipedia</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, D. Lobell, M. Burke, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/1905.02506">arXiv</a>
    <a href="https://www.ijcai.org/proceedings/2019/0502.pdf">PDF</a>
    <a href="https://github.com/buzkent86/WikiSatNet">Code</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">KDD 2019</div>
  <div class="paper-title">Predicting Economic Development using Geolocated Wikipedia Articles</div>
  <div class="paper-authors">E. Sheehan, C. Meng, M. Tan, <span class="me">B. Uzkent</span>, N. Jean, D. Lobell, M. Burke, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1905.01627.pdf">arXiv</a>
    <a href="https://dl.acm.org/doi/10.1145/3292500.3330784">PDF</a>
    <a href="https://github.com/uzkent/WikipediaPovertyMapping">Code</a>
  </div>
</div>

<div class="year-marker"><span>2018</span></div>

<div class="paper">
  <div class="paper-venue">WACV 2018</div>
  <div class="paper-title">EnKCF: Ensemble of Kernelized Correlation Filters for High-Speed Object Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, Y. Seo</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/1801.06729.pdf">arXiv</a>
    <a href="https://ieeexplore.ieee.org/document/8354233">PDF</a>
    <a href="https://github.com/buzkent86/EnKCF_Tracking_WACV18">Code</a>
  </div>
</div>

<div class="year-marker"><span>2017</span></div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2017</div>
  <div class="paper-title">Aerial Vehicle Tracking by Adaptive Fusion of Likelihood Maps</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Rangnekar, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8014769/">PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code">Code</a>
  </div>
</div>

<div class="year-marker"><span>2016</span></div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2016</div>
  <div class="paper-title">Real-time Target Detection and Tracking in Aerial Video using Hyperspectral Features</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/7789671">PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code">Code</a>
  </div>
</div>

<div class="year-marker"><span>2015</span></div>

<div class="paper">
  <div class="paper-venue">ICCS 2015</div>
  <div class="paper-title">Spectral Validation of Measurements in a Vehicle Tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/pii/S1877050915011667">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">SPIE 2015</div>
  <div class="paper-title">Background Image Understanding and Adaptive Imaging for Vehicle Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links"><a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9460/94600F/Background-image-understanding-and-adaptive-imaging-for-vehicle-tracking/10.1117/12.2177334.short">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">SPIE 2015</div>
  <div class="paper-title">Efficient Integration of Spectral Features for Vehicle Tracking utilizing an Adaptive Sensor</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links"><a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9407/1/Efficient-integration-of-spectral-features-for-vehicle-tracking-utilizing-an/10.1117/12.2082266.short">PDF</a></div>
</div>

<div class="year-marker"><span>2014</span></div>

<div class="paper">
  <div class="paper-venue">IEEE WNYIPW 2014</div>
  <div class="paper-title">3-D MRI Cardiac Segmentation using Graph Cuts</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, E. Cherry, N. Cahill</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/6999484">PDF</a>
    <a href="https://github.com/buzkent86/3D_MRI_Segmentation">Code</a>
  </div>
</div>

<div class="year-marker"><span>2013</span></div>

<div class="paper">
  <div class="paper-venue">ICCS 2013</div>
  <div class="paper-title">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061">PDF</a></div>
</div>

<div class="year-marker"><span>2011</span></div>

<div class="paper">
  <div class="paper-venue">IEEE ITNG 2011</div>
  <div class="paper-title">Pitch range-based feature extraction for audio surveillance systems</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana</div>
  <div class="paper-links"><a href="https://www.researchgate.net/profile/Buket_Barkana/publication/224245542_Pitch-Range_Based_Feature_Extraction_for_Audio_Surveillance_Systems/links/5654aa9808ae4988a7b055f7/Pitch-Range-Based-Feature-Extraction-for-Audio-Surveillance-Systems.pdf">PDF</a></div>
</div>

<div class="year-marker"><span>2010</span></div>

<div class="paper">
  <div class="paper-venue">EURO 2010</div>
  <div class="paper-title">Performances of the ANN, SVM, and K-means clustering methods recognizing different environmental sounds</div>
  <div class="paper-authors">B.D. Barkana, I. Saricicek, <span class="me">B. Uzkent</span></div>
</div>

<div class="year-marker"><span>2009</span></div>

<div class="paper">
  <div class="paper-venue">METU 2009</div>
  <div class="paper-title">Autonomous parallel parking of non-holonomic vehicles</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, O. Parlaktuna</div>
</div>

</div><!-- end timeline -->

<!-- ============================================================ -->
<!--                       JOURNAL PAPERS                         -->
<!-- ============================================================ -->

<h2 class="section-title" id="journals"><span class="icon">📖</span> Journal Articles <span class="section-count">(9)</span></h2>
<div class="section-line"></div>

<div class="timeline">

<div class="paper">
  <div class="paper-venue">Earth's Future · 2023</div>
  <div class="paper-title">Safe Shelter: A Case for Prioritizing Housing Quality in Climate Adaptation Policy by Remotely Sensing Roof Tarps in the San Francisco Bay Area</div>
  <div class="paper-authors">E. Velterop, <span class="me">B. Uzkent</span>, J. Suckale</div>
  <div class="paper-links"><a href="https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2022EF002789">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">IEEE TGRS · 2019</div>
  <div class="paper-title">Tracking in Aerial Hyperspectral Videos using Deep Kernelized Correlation Filters</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Rangnekar, M.J. Hoffman</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8435971">PDF</a>
    <a href="https://arxiv.org/pdf/1711.07235.pdf">arXiv</a>
    <a href="https://github.com/buzkent86/HKCF_Tracker">Code</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">IEEE JSTARS · 2016</div>
  <div class="paper-title">Integrating Hyperspectral Likelihoods in a Multi-dimensional Assignment Algorithm for Aerial Vehicle Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/7471414">PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code">Code</a>
    <a href="https://www.youtube.com/watch?v=scRQjEMGSRE">Video</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">IEEE Sensors Journal · 2015</div>
  <div class="paper-title">Feature Matching with an Adaptive Optical Sensor in a Ground Target Tracking System</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, Bin Chen</div>
  <div class="paper-links"><a href="https://ieeexplore.ieee.org/document/6873232/">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">Procedia Computer Science · 2013</div>
  <div class="paper-title">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">IJICIC · 2012</div>
  <div class="paper-title">Non-speech environmental sound classification using SVMS with a new set of features</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana, H. Cevikalp</div>
  <div class="paper-links"><a href="https://www.researchgate.net/profile/Hakan_Cevikalp/publication/267782696_Non-speech_environmental_sound_classification_using_SVMs_with_a_new_set_of_features/links/54b7bf9f0cf24eb34f6ed7ff/Non-speech-environmental-sound-classification-using-SVMs-with-a-new-set-of-features.pdf">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">Advanced Materials Research · 2012</div>
  <div class="paper-title">Normal and abnormal non-speech audio event detection using MFCC and PR-based feature sets</div>
  <div class="paper-authors">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
</div>

<div class="paper">
  <div class="paper-venue">Applied Acoustics · 2011</div>
  <div class="paper-title">Environmental noise classifier using a new set of feature parameters based on pitch range</div>
  <div class="paper-authors">B.D. Barkana, <span class="me">B. Uzkent</span>, I. Saricicek</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0003682X11001381">PDF</a></div>
</div>

<div class="paper">
  <div class="paper-venue">Expert Systems with Applications · 2011</div>
  <div class="paper-title">Automatic environmental noise source classification model using fuzzy logic</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana, J. Yang</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/pii/S0957417411001047">PDF</a></div>
</div>

</div><!-- end timeline -->

<!-- ============================================================ -->
<!--                  PREPRINTS & TECH REPORTS                    -->
<!-- ============================================================ -->

<h2 class="section-title" id="preprints"><span class="icon">📝</span> Preprints <span class="section-count">(2)</span></h2>
<div class="section-line"></div>

<div class="timeline">

<div class="paper">
  <div class="paper-venue">Preprint</div>
  <div class="paper-title">Domain Adaptation Using Adversarial Learning for Studying Low Resolution Images</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links"><a href="https://www.researchgate.net/publication/341030568_Adversarial_Domain_Adaptation_for_Analyzing_Low_Resolution_Images">ResearchGate</a></div>
</div>

<div class="paper">
  <div class="paper-venue">arXiv</div>
  <div class="paper-title">Learning to interpret satellite images using wikipedia</div>
  <div class="paper-authors">E. Sheehan, <span class="me">B. Uzkent</span>, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/1809.10236.pdf">arXiv</a></div>
</div>

</div><!-- end timeline -->

<p style="text-align: center; color: #9ca3af; font-size: 0.85rem; margin-top: 3rem; font-style: italic;">* denotes equal contribution</p>
