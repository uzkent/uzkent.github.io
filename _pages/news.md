---
title: ""
permalink: /news/
author_profile: true
redirect_from:
  - /news
---

{% include base_path %}

<style>
.news-header {
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
}
.news-header h1 { font-size: 1.8rem; margin: 0 0 0.3rem 0; color: #1a1a1a; }
.news-header-line { width: 100px; height: 3px; background: #2563eb; border-radius: 2px; margin-bottom: 0.5rem; }
.news-header p { color: #6b7280; font-size: 0.92rem; margin: 0; line-height: 1.5; }

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
  margin: 2rem 0 0.8rem 0;
}
.year-marker:first-child {
  margin-top: 0.5rem;
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
  font-size: 1.1rem;
  font-weight: 800;
  color: #1a1a1a;
}

/* News entries */
.news-item {
  position: relative;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 0.85rem 1.1rem;
  margin-bottom: 0.6rem;
}
.news-item::before {
  content: '';
  position: absolute;
  left: -24px;
  top: 1rem;
  width: 9px;
  height: 9px;
  background: #fff;
  border: 2.5px solid #2563eb;
  border-radius: 50%;
  z-index: 1;
}
.news-item.highlight {
  border-left: 3px solid #2563eb;
}

.news-text {
  font-size: 0.9rem;
  color: #374151;
  line-height: 1.5;
  margin: 0;
}
.news-text strong {
  color: #111827;
}

.news-links {
  display: flex;
  gap: 0.6rem;
  margin-top: 0.35rem;
  flex-wrap: wrap;
}
.news-links a {
  font-size: 0.76rem;
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}
.news-links a:hover { text-decoration: underline; }

.news-tag {
  display: inline-block;
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  margin-right: 0.4rem;
  vertical-align: middle;
}
.tag-paper { background: #dbeafe; color: #1e40af; }
.tag-patent { background: #fef3c7; color: #92400e; }
.tag-career { background: #d1fae5; color: #065f46; }
.tag-talk { background: #ede9fe; color: #5b21b6; }
.tag-award { background: #fce7f3; color: #9d174d; }
.tag-data { background: #f0fdf4; color: #166534; }
</style>

<div class="news-header">
  <h1>📰 News</h1>
  <div class="news-header-line"></div>
  <p>Latest updates on publications, patents, talks, and milestones.</p>
</div>

<div class="timeline">

<!-- ==================== 2026 ==================== -->
<div class="year-marker"><span>2026</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper submitted to <strong>ACL 2026</strong>.</p>
  <div class="news-links"><a href="https://arxiv.org/pdf/2601.04778">arXiv</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> Two papers submitted to <strong>ECCV 2026</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2510.02262">arXiv 1</a>
    <a href="https://arxiv.org/pdf/2603.25145">arXiv 2</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to the <strong>3rd CV4Smalls Workshop at CVPR 2026</strong> as the best paper candidate.</p>
  <div class="news-links"><a href="https://arxiv.org/pdf/2603.19481">arXiv</a></div>
</div>

<!-- ==================== 2025 ==================== -->
<div class="year-marker"><span>2025</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-patent">Patent</span> Two patents submitted in 2025.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-patent">Patent</span> Five patents accepted in 2025.</p>
  <div class="news-links">
    <a href="https://patents.google.com/patent/US12506850B2/en">Patent 1</a>
    <a href="https://patents.google.com/patent/US12468944B2/en">Patent 2</a>
    <a href="https://patents.google.com/patent/US12394190B2/en">Patent 3</a>
    <a href="https://patents.google.com/patent/US12386873B2/en">Patent 4</a>
    <a href="https://patents.google.com/patent/US12373698B2/en">Patent 5</a>
  </div>
</div>

<!-- ==================== 2024 ==================== -->
<div class="year-marker"><span>2024</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-patent">Patent</span> One patent accepted in 2024.</p>
  <div class="news-links"><a href="https://patents.google.com/patent/US12183062B2/en">Link</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>WACV 2024</strong>.</p>
  <div class="news-links"><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Yi_Augment_the_Pairs_Semantics-Preserving_Image-Caption_Pair_Augmentation_for_Grounding-Based_Vision_WACV_2024_paper.pdf">PDF</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>WACV 2024</strong>.</p>
  <div class="news-links"><a href="https://openaccess.thecvf.com/content/WACV2024/papers/Doshi_A_Multimodal_Benchmark_and_Improved_Architecture_for_Zero_Shot_Learning_WACV_2024_paper.pdf">PDF</a></div>
</div>

<!-- ==================== 2023 ==================== -->
<div class="year-marker"><span>2023</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>CVPR 2023</strong>.</p>
  <div class="news-links"><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Uzkent_Dynamic_Inference_With_Grounding_Based_Vision_and_Language_Models_CVPR_2023_paper.pdf">PDF</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>ICLR 2023</strong>.</p>
  <div class="news-links"><a href="https://openreview.net/pdf?id=UMERaIHMwB3">PDF</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>AAAI 2023</strong>.</p>
  <div class="news-links"><a href="https://arxiv.org/pdf/2301.05345.pdf">PDF</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>Earth's Future</strong> journal.</p>
  <div class="news-links"><a href="https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2022EF002789">PDF</a></div>
</div>

<!-- ==================== 2022 ==================== -->
<div class="year-marker"><span>2022</span></div>

<div class="news-item highlight">
  <p class="news-text"><span class="news-tag tag-career">Career</span> Joined <strong>Amazon</strong> as an Applied Scientist.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to a <strong>CVPR 2022 Workshop</strong>.</p>
  <div class="news-links"><a href="https://openaccess.thecvf.com/content/CVPR2022W/L3D-IVU/papers/Chakraborty_Efficient_Conditional_Pre-Training_for_Transfer_Learning_CVPRW_2022_paper.pdf">PDF</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>CVPR 2022</strong>.</p>
  <div class="news-links"><a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Lou_Lite-MDETR_A_Lightweight_Multi-Modal_Detector_CVPR_2022_paper.pdf">PDF</a></div>
</div>

<!-- ==================== 2021 ==================== -->
<div class="year-marker"><span>2021</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>ICCV 2021</strong>.</p>
  <div class="news-links">
    <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Ayush_Geography-Aware_Self-Supervised_Learning_ICCV_2021_paper.pdf">PDF</a>
    <a href="https://github.com/sustainlab-group/geography-aware-ssl">Code</a>
    <a href="https://geography-aware-ssl.github.io/">Project</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Seminar presentation at the <strong>Machine Learning for Remote Sensing</strong> group, University of Maryland.</p>
  <div class="news-links"><a href="../files/UMSeminar_Burak.pdf">Slides</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>ICLR 2021</strong>.</p>
  <div class="news-links">
    <a href="https://openreview.net/forum?id=Ovp8dvB8IBH">PDF</a>
    <a href="https://github.com/ermongroup/NDA">Code</a>
    <a href="https://www.youtube.com/watch?v=K-1mN2mz66k&t=21s&ab_channel=HenryAILabs">YouTube</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>AAAI 2021</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2006.08661.pdf">arXiv</a>
    <a href="https://github.com/sustainlab-group/mapillarygcn">Code</a>
    <a href="https://www.aaai.org/AAAI21Papers/AAAI-10056.LeeJ.pdf">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>AAAI 2021</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2006.04224.pdf">arXiv</a>
    <a href="https://www.aaai.org/AAAI21Papers/AAAI-10300.AyushK.pdf">PDF</a>
  </div>
</div>

<!-- ==================== 2020 ==================== -->
<div class="year-marker"><span>2020</span></div>

<div class="news-item highlight">
  <p class="news-text"><span class="news-tag tag-career">Career</span> Joined <strong>Samsung Research America</strong> as a Senior Research Scientist.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>CVPR 2020 Workshop</strong> on Agriculture-Vision.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2004.05471.pdf">arXiv</a>
    <a href="https://github.com/sustainlab-group/ParcelDelineation">Code</a>
    <a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>IJCAI 2020</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2002.01612.pdf">arXiv</a>
    <a href="https://www.ijcai.org/Proceedings/2020/0608.pdf">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Presentation at <strong>Qualcomm HQ</strong> in San Diego.</p>
  <div class="news-links"><a href="../files/Qualcomm.pdf">Slides</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>CVPR 2020</strong> (Oral).</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/2003.00425.pdf">arXiv</a>
    <a href="https://github.com/ermongroup/PatchDrop">Code</a>
    <a href="https://www.youtube.com/watch?v=n0HGh2x6Cgg">Video</a>
    <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Uzkent_Learning_When_and_Where_to_Zoom_With_Deep_Reinforcement_Learning_CVPR_2020_paper.pdf">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Presentation at <strong>Planet Labs HQ</strong> in San Francisco.</p>
  <div class="news-links"><a href="../files/Planet_Presentation.pdf">Slides</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Seminar presentation at <strong>Sabanci University</strong>, Turkey.</p>
  <div class="news-links">
    <a href="https://mfg.sabanciuniv.edu/tr/events-detail/21371">Abstract</a>
    <a href="../files/Sabanci_Seminar.pdf">Slides</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>WACV 2020</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/1912.06838.pdf">arXiv</a>
    <a href="https://github.com/VSAnimator/stgan">Code</a>
    <a href="https://openaccess.thecvf.com/content_WACV_2020/papers/Sarukkai_Cloud_Removal_from_Satellite_Images_using_Spatiotemporal_Generator_Networks_WACV_2020_paper.pdf">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>WACV 2020</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/1912.03966.pdf">arXiv</a>
    <a href="https://github.com/uzkent/EfficientObjectDetection">Code</a>
    <a href="../files/WACV_Short.pdf">Slides</a>
  </div>
</div>

<!-- ==================== 2019 ==================== -->
<div class="year-marker"><span>2019</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Presentation at <strong>University of California at San Diego</strong>.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>IJCAI 2019</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/1905.02506.pdf">arXiv</a>
    <a href="https://github.com/uzkent/WikiSatNet">Code</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>KDD 2019</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/1905.01627.pdf">arXiv</a>
    <a href="https://github.com/uzkent/WikipediaPovertyMapping">Code</a>
    <a href="https://dl.acm.org/doi/10.1145/3292500.3330784">PDF</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Presentation at <strong>Orbital Insight</strong>.</p>
  <div class="news-links"><a href="../files/Orbital_Insight_Presentation.pdf">Slides</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>IEEE Transactions on Geoscience and Remote Sensing</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/abs/1711.07235">arXiv</a>
    <a href="https://github.com/uzkent/HKCF_Tracker">Code</a>
  </div>
</div>

<!-- ==================== 2018 ==================== -->
<div class="year-marker"><span>2018</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-talk">Talk</span> Seminar presentation at <strong>Carnegie Mellon University VASC</strong>.</p>
  <div class="news-links">
    <a href="https://www.ri.cmu.edu/event/object-detection-and-tracking-on-low-resolution-aerial-images/">Abstract</a>
    <a href="../files/CMU_VSAR_Seminar.pdf">Slides</a>
  </div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>WACV 2018</strong>.</p>
  <div class="news-links">
    <a href="https://arxiv.org/pdf/1801.06729.pdf">arXiv</a>
    <a href="https://github.com/uzkent/EnKCF_Tracker">Code</a>
    <a href="../files/WACV18_Presentation.pdf">Slides</a>
    <a href="../files/WACV18_Poster.pdf">Poster</a>
    <a href="https://www.youtube.com/embed/dWeIbECiVkY?ecver=1">Demo 1</a>
    <a href="https://www.youtube.com/embed/ZCnAjxJkseY?ecver=1">Demo 2</a>
    <a href="https://www.youtube.com/embed/hAxA903YH2Y?ecver=1">Demo 3</a>
    <a href="https://www.youtube.com/embed/h-yXx1A2dL0?ecver=1">Demo 4</a>
  </div>
</div>

<!-- ==================== 2017 ==================== -->
<div class="year-marker"><span>2017</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>CVPR 2017 Workshop</strong> on Perception Beyond the Visible Spectrum.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-data">Dataset</span> Released <strong>Hyperspectral Aerial Video Dataset</strong> for vehicle tracking.</p>
  <div class="news-links">
    <a href="https://uzkent.github.io/datasets/">Dataset</a>
    <a href="https://github.com/uzkent/CVPRW17_Paper_Code">Code</a>
  </div>
</div>

<!-- ==================== 2016 ==================== -->
<div class="year-marker"><span>2016</span></div>

<div class="news-item highlight">
  <p class="news-text"><span class="news-tag tag-award">Milestone</span> Defended <strong>Ph.D. thesis</strong> on "Aerial Vehicle Tracking using a Multi-modal Optical Sensor".</p>
  <div class="news-links"><a href="../files/Thesis.Defense.pdf">Slides</a></div>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-career">Career</span> Completed internship at <strong>Huawei R&D</strong>.</p>
</div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper accepted to <strong>IEEE Journal of Selected Topics in Remote Sensing and Observation</strong>.</p>
  <div class="news-links"><a href="https://www.youtube.com/watch?v=scRQjEMGSRE">Video</a></div>
</div>

<!-- ==================== 2014 ==================== -->
<div class="year-marker"><span>2014</span></div>

<div class="news-item">
  <p class="news-text"><span class="news-tag tag-paper">Paper</span> One paper presented at <strong>IEEE Western New York Image Processing Workshop</strong>.</p>
  <div class="news-links"><a href="https://github.com/uzkent/3D_MRI_Segmentation">Code</a></div>
</div>

</div><!-- end timeline -->
