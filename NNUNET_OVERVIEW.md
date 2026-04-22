# nnU-Net: The Self-Configuring Framework for Medical Imaging

## 1. What is nnU-Net?
**nnU-Net** (no-new-Net) is a state-of-the-art framework for medical image segmentation that automatically configures its entire pipeline—including preprocessing, network architecture, training, and post-processing—based on the specific characteristics of any given dataset. It eliminates the need for manual hyperparameter tuning while consistently outperforming hand-crafted solutions in medical imaging competitions.

### Core Principles:
- **Rule-based Parameters:** Automatically determines image normalization, resampling, and patch sizes.
- **U-Net Evolution:** Uses a standardized 2D, 3D low-resolution, and 3D full-resolution U-Net architecture.
- **Ensemble Learning:** Often combines multiple folds and architectures to achieve maximum robustness.

---

## 2. Project Implementation: Anatomical Digital Twin
In this project, we utilized nnU-Net to build a high-precision segmentation pipeline for multi-organ analysis, serving as the backbone for the **MED-AI 3D Dashboard**.

### Targeted Anatomical Structures:
1.  **Heart (Left Atrium):** For cardiac structural analysis.
2.  **Spleen:** For abdominal organ volume estimation.
3.  **Prostate:** For dual-zone (PZ/TZ) differentiation in oncology.
4.  **Hippocampus:** For sub-millimetric brain region mapping.

---

## 3. Our Workflow & Operations

### Step 1: Data Standardization
We converted raw DICOM/NIfTI scans into the **nnU-Net format** (Dataset IDs 002, 004, 005, and 009), ensuring proper orientation and metadata preservation.

### Step 2: Training & Inference
- **Model:** 3D Full-Resolution U-Net.
- **Strategy:** Cross-validation across 5 folds to ensure generalization.
- **Inference:** Generated dense voxel masks for new, unseen clinical cases.

### Step 3: Morphological Post-Processing
To bridge the gap between AI voxel output and usable 3D models, we implemented a custom refinement pipeline:
- **Binary Hole Filling:** Ensures organs are solid for accurate volume calculation.
- **Binary Opening:** Removes "salt" noise and floating artifacts (disconnected voxels).
- **Binary Closing:** Smoothes the surface boundaries of the segmented organs.

### Step 4: 3D Mesh Optimization
The refined masks were converted into **Optimized Meshes** using the Marching Cubes algorithm, reducing vertex count by **~8%** while improving rendering speed to **90+ FPS**.

---

## 4. Key Results
- **Accuracy:** Achieved a mean Dice Similarity Coefficient of **>90%** across core organs.
- **Visualization:** Integrated water-tight, manifold meshes into a React + Three.js dashboard for real-time interaction.
- **Clinical Readiness:** Significantly reduced noise in segmentations, preventing visual artifacts in diagnostic reviews.

---
*This repository contains the complete pipeline from raw AI training to refined 3D digital twins.*
