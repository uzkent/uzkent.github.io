---
title: "Publications"
permalink: /publications/
author_profile: true
redirect_from:
  - /publications
---

{% include base_path %}

<style>
.pub-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e5e7eb;
}
.pub-header h1 { font-size: 1.8rem; margin: 0 0 0.5rem 0; color: #1a1a1a; }
.pub-header p { color: #6b7280; font-size: 0.95rem; margin: 0; line-height: 1.6; }

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

.section-title {
  font-size: 1.3rem;
  color: #1a1a1a;
  margin: 2.5rem 0 0.5rem 0;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid #d1d5db;
  scroll-margin-top: 80px;
}
.section-count {
  font-size: 0.8rem;
  color: #9ca3af;
  font-weight: 400;
}

.year-label {
  font-size: 1rem;
  font-weight: 700;
  color: #374151;
  margin: 1.5rem 0 0.6rem 0;
}

.paper {
  margin-bottom: 1rem;
  padding: 0.8rem 0;
  border-bottom: 1px solid #f3f4f6;
}
.paper:last-child { border-bottom: none; }

.paper-venue {
  font-size: 0.75rem;
  font-weight: 700;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.paper-venue .oral-tag {
  color: #dc2626;
  font-weight: 700;
}
.paper-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: #111827;
  margin: 0.2rem 0;
  line-height: 1.4;
}
.paper-authors {
  font-size: 0.85rem;
  color: #6b7280;
  line-height: 1.4;
}
.paper-authors .me {
  font-weight: 700;
  color: #111827;
}
.paper-links {
  display: flex;
  gap: 0.8rem;
  margin-top: 0.3rem;
  flex-wrap: wrap;
}
.paper-links a {
  font-size: 0.78rem;
  color: #2563eb;
  text-decoration: none;
  font-weight: 500;
}
.paper-links a:hover { text-decoration: underline; }
</style>

<div class="pub-header">
  <p>
    Research in computer vision, efficient deep learning, multi-modal models, and remote sensing. 43 publications across conferences, journals, and preprints.
  </p>
</div>

<div class="pub-nav">
  <a href="#conferences">Conference Papers (29)</a>
  <a href="#journals">Journal Articles (9)</a>
  <a href="#preprints">Preprints (5)</a>
</div>

<!-- ============================================================ -->
<!--                     CONFERENCE PAPERS                        -->
<!-- ============================================================ -->

<h2 class="section-title" id="conferences">Conference Papers <span class="section-count">(29)</span></h2>

<div class="year-label">2024</div>

<div class="paper">
  <div class="paper-venue">WACV 2024</div>
  <div class="paper-title">A Multimodal Benchmark and Improved Architecture for Zero Shot Learning</div>
  <div class="paper-authors">K. Doshi, A. Garg, <span class="me">B. Uzkent</span>, X. Wang, M. Omar</div>
</div>

<div class="paper">
  <div class="paper-venue">WACV 2024</div>
  <div class="paper-title">Augment the Pairs: Semantics-Preserving Image-Caption Pair Augmentation for Grounding-Based Vision and Language Models</div>
  <div class="paper-authors">J. Yi, <span class="me">B. Uzkent</span>, O. Ignat, Z. Li, A. Garg, X. Yu, L. Liu</div>
</div>

<div class="year-label">2023</div>

<div class="paper">
  <div class="paper-venue">CVPR 2023</div>
  <div class="paper-title">Dynamic Inference with Grounding Based Vision and Language Models</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Garg, W. Zhou, K. Doshi, J. Yi, X. Wang, M. Omar</div>
</div>

<div class="paper">
  <div class="paper-venue">AAAI 2023</div>
  <div class="paper-title">GOHSP: A Unified Framework of Graph and Optimization-based Heterogeneous Structured Pruning for Vision Transformer</div>
  <div class="paper-authors">M. Yin, <span class="me">B. Uzkent</span>, Y. Shen, H. Jin</div>
</div>

<div class="paper">
  <div class="paper-venue">ICLR 2023</div>
  <div class="paper-title">Learning to Jointly Share and Prune Weights for Grounding Based Vision and Language Models</div>
  <div class="paper-authors">S. Gao, <span class="me">B. Uzkent</span>, Y. Shen, H. Huang, H. Jin</div>
</div>

<div class="year-label">2022</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2022</div>
  <div class="paper-title">Efficient Conditional Pre-training for Transfer Learning</div>
  <div class="paper-authors">S. Chakraborty, <span class="me">B. Uzkent</span>, K. Ayush, E. Sheehan, S. Ermon</div>
  <div class="paper-links"><a href="https://arxiv.org/abs/2011.10231">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR 2022</div>
  <div class="paper-title">Lite-MDETR: A Lightweight Multi-Modal Detector</div>
  <div class="paper-authors">Q. Lu, Y.C. Shu, <span class="me">B. Uzkent</span>, T. Hua, Y. Shen, H. Jin</div>
</div>

<div class="year-label">2021</div>

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
  <div class="paper-links"><a href="https://arxiv.org/pdf/2006.04224.pdf">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">AAAI 2021</div>
  <div class="paper-title">Predicting Geo-attributes Using Deep Learning and Publicly Available Street-level Images</div>
  <div class="paper-authors">J. Lee, D. Grosz, <span class="me">B. Uzkent</span>, S. Zheng, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://arxiv.org/pdf/2006.08661.pdf">arXiv</a>
    <a href="https://github.com/sustainlab-group/mapillarygcn">Code</a>
  </div>
</div>

<div class="year-label">2020</div>

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
  </div>
</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2020</div>
  <div class="paper-title">Farmland Parcel Delineation using Spatio-temporal Convolutional Networks</div>
  <div class="paper-authors">H.L. Aung, <span class="me">B. Uzkent</span>, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links">
    <a href="https://openaccess.thecvf.com/content_CVPRW_2020/papers/w5/Aung_Farm_Parcel_Delineation_Using_Spatio-Temporal_Convolutional_Networks_CVPRW_2020_paper.pdf">PDF</a>
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

<div class="year-label">2019</div>

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
    <a href="https://dl.acm.org/citation.cfm?id=3330784">PDF</a>
    <a href="https://github.com/buzkent86/WikipediaPovertyMapping">Code</a>
  </div>
</div>

<div class="year-label">2018</div>

<div class="paper">
  <div class="paper-venue">WACV 2018</div>
  <div class="paper-title">EnKCF: Ensemble of Kernelized Correlation Filters for High-Speed Object Tracking</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, Y. Seo</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8354233">PDF</a>
    <a href="https://github.com/buzkent86/EnKCF_Tracking_WACV18">Code</a>
  </div>
</div>

<div class="year-label">2017</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2017</div>
  <div class="paper-title">Aerial Vehicle Tracking by Adaptive Fusion of Likelihood Maps</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, A. Rangnekar, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/8014769/">PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code">Code</a>
  </div>
</div>

<div class="year-label">2016</div>

<div class="paper">
  <div class="paper-venue">CVPR Workshop 2016</div>
  <div class="paper-title">Real-time Target Detection and Tracking in Aerial Video using Hyperspectral Features</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/7789671">PDF</a>
    <a href="https://github.com/buzkent86/CVPRW17_Paper_code">Code</a>
  </div>
</div>

<div class="year-label">2015</div>

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

<div class="year-label">2014</div>

<div class="paper">
  <div class="paper-venue">IEEE WNYIPW 2014</div>
  <div class="paper-title">3-D MRI Cardiac Segmentation using Graph Cuts</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, E. Cherry, N. Cahill</div>
  <div class="paper-links">
    <a href="https://ieeexplore.ieee.org/document/6999484">PDF</a>
    <a href="https://github.com/buzkent86/3D_MRI_Segmentation">Code</a>
  </div>
</div>

<div class="year-label">2013</div>

<div class="paper">
  <div class="paper-venue">ICCS 2013</div>
  <div class="paper-title">Feature matching and adaptive prediction models in an object tracking DDDAS</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, M. J. Hoffman, A. Vodacek, J. P. Kerekes, B. Chen</div>
  <div class="paper-links"><a href="https://www.sciencedirect.com/science/article/pii/S1877050913005061">PDF</a></div>
</div>

<div class="year-label">2011</div>

<div class="paper">
  <div class="paper-venue">IEEE ITNG 2011</div>
  <div class="paper-title">Pitch range-based feature extraction for audio surveillance systems</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, B.D. Barkana</div>
  <div class="paper-links"><a href="https://www.researchgate.net/profile/Buket_Barkana/publication/224245542_Pitch-Range_Based_Feature_Extraction_for_Audio_Surveillance_Systems/links/5654aa9808ae4988a7b055f7/Pitch-Range-Based-Feature-Extraction-for-Audio-Surveillance-Systems.pdf">PDF</a></div>
</div>

<div class="year-label">2010</div>

<div class="paper">
  <div class="paper-venue">EURO 2010</div>
  <div class="paper-title">Performances of the ANN, SVM, and K-means clustering methods recognizing different environmental sounds</div>
  <div class="paper-authors">B.D. Barkana, I. Saricicek, <span class="me">B. Uzkent</span></div>
</div>

<div class="year-label">2009</div>

<div class="paper">
  <div class="paper-venue">METU 2009</div>
  <div class="paper-title">Autonomous parallel parking of non-holonomic vehicles</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, O. Parlaktuna</div>
</div>

<!-- ============================================================ -->
<!--                       JOURNAL PAPERS                         -->
<!-- ============================================================ -->

<h2 class="section-title" id="journals">Journal Articles <span class="section-count">(9)</span></h2>

<div class="paper">
  <div class="paper-venue">Earth's Future · 2022</div>
  <div class="paper-title">Safe Shelter: A Case for Prioritizing Housing Quality in Climate Adaptation Policy by Remotely Sensing Roof Tarps in the San Francisco Bay Area</div>
  <div class="paper-authors">E. Velterop, <span class="me">B. Uzkent</span>, J. Suckale</div>
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

<!-- ============================================================ -->
<!--                  PREPRINTS & TECH REPORTS                    -->
<!-- ============================================================ -->

<h2 class="section-title" id="preprints">Preprints <span class="section-count">(5)</span></h2>

<div class="paper">
  <div class="paper-venue">arXiv · 2025</div>
  <div class="paper-title">CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models</div>
  <div class="paper-authors">T. Poppi, <span class="me">B. Uzkent</span>, A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, R. Cucchiara, F. Schiffers</div>
  <div class="paper-links"><a href="https://arxiv.org/abs/2601.04778">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">arXiv · 2025</div>
  <div class="paper-title">From Frames to Clips: Efficient Key Clip Selection for Long-Form Video Understanding</div>
  <div class="paper-authors">G. Sun, A. Singhal, <span class="me">B. Uzkent</span>, M. Shah, C. Chen, G. Kessler</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2510.02262">arXiv</a>
    <a href="https://guangyusun.com/f2c/">Project</a>
  </div>
</div>

<div class="paper">
  <div class="paper-venue">Preprint</div>
  <div class="paper-title">Domain Adaptation Using Adversarial Learning for Studying Low Resolution Images</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, S. Ermon</div>
  <div class="paper-links"><a href="https://www.researchgate.net/publication/341030568_Adversarial_Domain_Adaptation_for_Analyzing_Low_Resolution_Images">ResearchGate</a></div>
</div>

<div class="paper">
  <div class="paper-venue">arXiv</div>
  <div class="paper-title">Learning to Interpret Satellite Images in Global Scale Using Wikipedia</div>
  <div class="paper-authors"><span class="me">B. Uzkent</span>, E. Sheehan, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/1905.02506.pdf">arXiv</a></div>
</div>

<div class="paper">
  <div class="paper-venue">arXiv</div>
  <div class="paper-title">Learning to interpret satellite images using wikipedia</div>
  <div class="paper-authors">E. Sheehan, <span class="me">B. Uzkent</span>, C. Meng, Z. Tang, M. Burke, D. Lobell, S. Ermon</div>
  <div class="paper-links"><a href="https://arxiv.org/pdf/1809.10236.pdf">arXiv</a></div>
</div>

<p style="text-align: center; color: #9ca3af; font-size: 0.85rem; margin-top: 3rem; font-style: italic;">* denotes equal contribution</p>
