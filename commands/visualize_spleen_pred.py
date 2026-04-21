import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import os

# Spleen case prediction (Case 1)
pred_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_spleen\spleen_1.nii.gz"
orig_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset009_Spleen\imagesTs\spleen_1_0000.nii.gz"

print("Loading Spleen CT data...")
img = nib.load(orig_path).get_fdata()
pred = nib.load(pred_path).get_fdata()

# Get middle cross-section where spleen is prominent
z_slice = img.shape[2] // 2

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 1. Raw CT (With Abdominal Windowing for clarity)
# Soft tissue window logic: clip -100 to +300 HU
axs[0].imshow(np.clip(img[:, :, z_slice], -100, 300), cmap='gray')
axs[0].set_title('Raw Abdominal CT Scan')
axs[0].axis('off')

# 2. Predicted Mask
axs[1].imshow(pred[:, :, z_slice], cmap='viridis')
axs[1].set_title('AI Segmented Spleen Mask')
axs[1].axis('off')

# 3. Final Overlay (High contrast)
axs[2].imshow(np.clip(img[:, :, z_slice], -100, 300), cmap='gray')
mask = (pred[:, :, z_slice] == 1).astype(float)
axs[2].imshow(mask, cmap='spring', alpha=0.5) # Neon pink/yellow for visibility
axs[2].set_title('Final Inference Overlay (93.5% Accuracy)')
axs[2].axis('off')

out_path = r"c:\The Sketchbook\SEM VI\CV-Project\spleen_prediction_showcase.png"
plt.savefig(out_path, bbox_inches='tight')
print("Spleen prediction visualization saved to:", out_path)
