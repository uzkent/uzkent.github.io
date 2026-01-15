---
title: ""
permalink: /datasets/
author_profile: true
redirect_from:
  - /datasets
---

{% include base_path %}

# Datasets

---

## 🌍 Predicting Geoattributes with Street-Level Images

Dataset for predicting geoattributes using **Mapillary street-level images**.

[![GitHub](https://img.shields.io/badge/GitHub-Code-blue?style=flat-square&amp;logo=github)](https://github.com/sustainlab-group/mapillarygcn)

---

## ☁️ Cloud Removal in Satellite Imagery

Paired and unpaired **cloudy and cloud-free satellite images** for training generative models to remove clouds.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=flat-square&amp;logo=github)](https://github.com/VSAnimator/stgan)

---

## 🚗 Synthetic Aerial Vehicle Classification Dataset

A synthetic dataset for aerial vehicle detection and classification, designed for **Wide Area Motion Imagery (WAMI)** applications.

### Overview

| Attribute | Details |
|-----------|---------|
| **Total Samples** | 55,226 images |
| **Resolution** | 64×64 px |
| **Classes** | Vehicle (27,613) • Background (27,613) |
| **Ground Sampling Distance** | ~0.3m |
| **Generator** | DIRSIG (Rochester Institute of Technology) |

### Download

📥 [**DIRSIG Training + WAMI Validation Images**](https://drive.google.com/open?id=1cQIM2a7gNaxlE2oFdQ_O-GqgBo84fLia)

**Contents:**
- `train_dirsig/` — Synthetic images + labels
- `validation_wami/` — 600 real WAMI images + labels

### Sample Images

![Dataset Samples](../images/positives_vehicle_detection.jpg)
*Left: DIRSIG synthetic samples | Right: WAMI validation samples*

### Citation

```bibtex
@article{uzkent2017tracking,
    title={Tracking in Aerial Hyperspectral Videos using Deep Kernelized Correlation Filters},
    author={Uzkent, Burak and Rangnekar, Aneesh and Hoffman, Matthew J},
    journal={arXiv preprint arXiv:1711.07235},
    year={2017}
}
