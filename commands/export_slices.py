import nibabel as nib
import numpy as np
import os
from PIL import Image

def export_slices(nii_path, output_dir, organ_name):
    print(f"Exporting slices for {organ_name} from {nii_path}...")
    img = nib.load(nii_path)
    data = img.get_fdata()
    
    # Normalize data for visualization (0-255)
    data = np.clip(data, np.percentile(data, 5), np.percentile(data, 95))
    data = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Export 15 equally spaced slices for smoother scrubbing
    num_slices = data.shape[2]
    indices = np.linspace(0, num_slices - 1, 15).astype(int)
    
    for count, i in enumerate(indices):
        slice_data = data[:, :, i]
        # Rotate to match standard medical orientation
        slice_data = np.rot90(slice_data)
        img_slice = Image.fromarray(slice_data)
        img_slice.save(os.path.join(output_dir, f"{organ_name.lower()}_{count}.png"))
    
    return 15

# Spleen Original Image (example)
tasks = [
    {
        "name": "Spleen",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset009_Spleen\imagesTs\spleen_1_0000.nii.gz",
    },
    {
        "name": "Heart",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset002_Heart\imagesTs\la_001_0000.nii.gz",
    },
    {
        "name": "Prostate",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset005_Prostate\imagesTs\prostate_03_0000.nii.gz",
    },
    {
        "name": "Hippocampus",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset004_Hippocampus\imagesTs\hippocampus_002_0000.nii.gz",
    }
]

output_base = r"c:\The Sketchbook\SEM VI\CV-Project\3d-medical-dashboard\public\models\slices"

for task in tasks:
    if os.path.exists(task["path"]):
        export_slices(task["path"], output_base, task["name"])
    else:
        print(f"Skipping {task['name']}, path not found.")
