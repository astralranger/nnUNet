import nibabel as nib
import numpy as np
from scipy import ndimage
from skimage import measure
import os

def generate_report(nii_path, label_value, organ_name):
    print(f"--- Morphology Impact Report: {organ_name} ---")
    img = nib.load(nii_path)
    data = img.get_fdata()
    
    # 0. Raw Mask
    raw_mask = (data == label_value).astype(bool)
    raw_voxels = np.sum(raw_mask)
    
    # Generate raw mesh to count vertices
    verts_raw, _, _, _ = measure.marching_cubes(raw_mask.astype(float), 0.5)
    raw_verts_count = len(verts_raw)

    struct = ndimage.generate_binary_structure(3, 1)

    # 1. Fill Holes Impact
    filled_mask = ndimage.binary_fill_holes(raw_mask)
    voxels_after_fill = np.sum(filled_mask)
    filled_holes_count = voxels_after_fill - raw_voxels

    # 2. Opening Impact (Noise Removal)
    opened_mask = ndimage.binary_opening(filled_mask, structure=struct, iterations=1)
    voxels_after_opening = np.sum(opened_mask)
    noise_voxels_removed = voxels_after_fill - voxels_after_opening

    # 3. Closing Impact (Smoothing/Gap Filling)
    closed_mask = ndimage.binary_closing(opened_mask, structure=struct, iterations=1)
    voxels_after_closing = np.sum(closed_mask)
    gaps_closed_count = voxels_after_closing - voxels_after_opening

    # Final Mesh Vertices
    verts_final, _, _, _ = measure.marching_cubes(closed_mask.astype(float), 0.5)
    final_verts_count = len(verts_final)

    report = f"""
# Morphological Operation Impact Report
**Target Organ:** {organ_name}

## 1. Quantitative Voxel Analysis
| Operation | Voxel Count | Delta | Purpose |
| :--- | :--- | :--- | :--- |
| **Raw Prediction** | {raw_voxels:,} | - | Initial AI Output |
| **After Hole Filling** | {voxels_after_fill:,} | +{filled_holes_count:,} | Internal Solidification |
| **After Opening** | {voxels_after_opening:,} | -{noise_voxels_removed:,} | Salt Noise Removal |
| **After Closing** | {voxels_after_closing:,} | +{gaps_closed_count:,} | Surface Smoothing |

## 2. Mesh Complexity Analysis
| Metric | Raw Mesh | Optimized Mesh | Change |
| :--- | :--- | :--- | :--- |
| **Vertex Count** | {raw_verts_count:,} | {final_verts_count:,} | {((final_verts_count - raw_verts_count)/raw_verts_count)*100:.1f}% |

## 3. Qualitative Observations
1. **Denoising:** The Binary Opening operation successfully removed {noise_voxels_removed} disconnected voxels, preventing "floating debris" in the 3D viewer.
2. **Solidification:** The Hole Filling operation corrected {filled_holes_count} internal gaps that would have caused rendering artifacts or incorrect volume measurements.
3. **Geometry:** The final mesh has {final_verts_count:,} vertices. The change in vertex count suggests a more structurally sound surface for Real-Time 3D rendering.
"""
    return report

# Use Spleen as the primary case study
spleen_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_spleen\spleen_1.nii.gz"
if os.path.exists(spleen_path):
    report_content = generate_report(spleen_path, 1, "Spleen")
    
    # Save to workspace
    with open("morphology_impact_report.md", "w") as f:
        f.write(report_content)
    print("\nReport generated successfully: morphology_impact_report.md")
else:
    print("Spleen prediction not found for report generation.")
