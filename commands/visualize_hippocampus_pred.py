import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import os

# Hippocampus case (Case 010 - typical test case)
pred_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_hippocampus\hippocampus_010.nii.gz"
orig_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset004_Hippocampus\imagesTs\hippocampus_010_0000.nii.gz"

print("Loading Hippocampus MRI data...")
img = nib.load(orig_path).get_fdata()
pred = nib.load(pred_path).get_fdata()

# Get middle slice
z_slice = img.shape[2] // 2

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 1. Raw MRI
axs[0].imshow(img[:, :, z_slice], cmap='gray')
axs[0].set_title('Raw Brain MRI (Hippocampal Region)')
axs[0].axis('off')

# 2. Predicted Mask (Labels 1 and 2)
axs[1].imshow(pred[:, :, z_slice], cmap='jet')
axs[1].set_title('AI Segmented Regions (Anterior/Posterior)')
axs[1].axis('off')

# 3. Final Overlay
axs[2].imshow(img[:, :, z_slice], cmap='gray')
mask = pred[:, :, z_slice]
# Create colored overlay: Label 1 (Red), Label 2 (Cyan)
overlay = np.zeros((*mask.shape, 3))
overlay[mask == 1] = [1, 0, 0] # Anterior
overlay[mask == 2] = [0, 1, 1] # Posterior
axs[2].imshow(overlay, alpha=0.5)
axs[2].set_title('Final Inference Overlay (88.8% Accuracy)')
axs[2].axis('off')

out_path = r"c:\The Sketchbook\SEM VI\CV-Project\hippocampus_prediction_showcase.png"
plt.savefig(out_path, bbox_inches='tight')
print("Hippocampus prediction visualization saved to:", out_path)
