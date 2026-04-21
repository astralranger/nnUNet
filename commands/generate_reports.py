import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# Config
case_ids = ['la_007', 'la_016', 'la_021', 'la_024']
dice_scores = [0.898, 0.946, 0.908, 0.913] # Extracted from summary.json
base_pred = r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results\Dataset002_Heart\nnUNetTrainer__nnUNetPlans__3d_fullres\fold_0\validation"
base_raw = r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset002_Heart\imagesTr"

def create_report(case_id, score, index):
    # Load Image (MRI) and Label (AI Prediction)
    img_path = os.path.join(base_raw, f"{case_id}_0000.nii.gz")
    pred_path = os.path.join(base_pred, f"{case_id}.nii.gz")
    
    img = nib.load(img_path).get_fdata()
    pred = nib.load(pred_path).get_fdata()
    
    z_slice = img.shape[2] // 2
    
    fig = plt.figure(figsize=(18, 6))
    
    # 1. Raw Image
    ax1 = fig.add_subplot(1, 4, 1)
    ax1.imshow(img[:, :, z_slice], cmap='gray')
    ax1.set_title(f'Raw MRI ({case_id})')
    ax1.axis('off')
    
    # 2. Overlay
    ax2 = fig.add_subplot(1, 4, 2)
    ax2.imshow(img[:, :, z_slice], cmap='gray')
    ax2.imshow(pred[:, :, z_slice], cmap='jet', alpha=0.5)
    ax2.set_title('AI Prediction Overlay')
    ax2.axis('off')
    
    # 3. Dice Score Bar (Single)
    ax3 = fig.add_subplot(1, 4, 3)
    ax3.bar(['Dice Score'], [score], color='skyblue')
    ax3.set_ylim(0, 1)
    ax3.set_title(f'Accuracy: {score*100:.1f}%')
    for i, v in enumerate([score]):
        ax3.text(i, v + 0.02, f"{v:.3f}", ha='center', fontweight='bold')

    # 4. Global Score comparison (Multiple)
    ax4 = fig.add_subplot(1, 4, 4)
    ax4.bar(case_ids, dice_scores, color=['lightgrey', 'lightgrey', 'lightgrey', 'lightgrey'])
    ax4.patches[index].set_color('blue') # Highlight current case
    ax4.set_ylim(0.8, 1.0)
    ax4.set_title('Model Performance across cases')
    plt.xticks(rotation=45)

    plt.tight_layout()
    out_file = f"c:\\The Sketchbook\\SEM VI\\CV-Project\\report_{case_id}.png"
    plt.savefig(out_file, dpi=120)
    print(f"Generated report for {case_id}")

for i, cid in enumerate(case_ids):
    create_report(cid, dice_scores[i], i)
