import nibabel as nib
import numpy as np
from skimage import measure
from scipy import ndimage
import json
import os

def export_mesh(nii_path, label_value, output_json, organ_name, apply_morphology=True):
    print(f"Loading {nii_path} (Morphology: {apply_morphology})...")
    img = nib.load(nii_path)
    data = img.get_fdata()
    
    # Extract the mask for the specific label
    mask = (data == label_value).astype(bool)
    
    if np.sum(mask) == 0:
        print(f"Warning: No voxels found for label {label_value} in {nii_path}")
        return

    if apply_morphology:
        # --- EXPLICIT MORPHOLOGICAL OPERATIONS ---
        print(f"Applying morphological operations to {organ_name}...")
        mask = ndimage.binary_fill_holes(mask)
        struct = ndimage.generate_binary_structure(3, 1)
        mask = ndimage.binary_opening(mask, structure=struct, iterations=1)
        mask = ndimage.binary_closing(mask, structure=struct, iterations=1)
    
    # Convert back to float for marching cubes
    mask = mask.astype(float)
    
    # Marching Cubes
    print(f"Generating mesh for {organ_name}...")
    verts, faces, normals, values = measure.marching_cubes(mask, 0.5)
    
    # Normalize vertices to be centered and scaled reasonably for Three.js
    center = verts.mean(axis=0)
    verts = verts - center
    max_dist = np.max(np.linalg.norm(verts, axis=1))
    verts = verts / max_dist
    
    # Convert to list for JSON
    mesh_data = {
        "organ": organ_name,
        "vertices": verts.flatten().tolist(),
        "faces": faces.flatten().tolist(),
        "metadata": {
            "voxels": int(np.sum(mask)),
            "center": center.tolist(),
            "is_refined": apply_morphology
        }
    }
    
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w') as f:
        json.dump(mesh_data, f)
    print(f"Exported {organ_name} to {output_json}")

# Tasks and their predictions
tasks = [
    {
        "name": "Spleen",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_spleen\spleen_1.nii.gz",
        "label": 1
    },
    {
        "name": "Heart",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions\la_001.nii.gz",
        "label": 1
    },
    {
        "name": "Prostate",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_prostate\prostate_03.nii.gz",
        "label": 1
    },
    {
        "name": "Hippocampus",
        "path": r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_hippocampus\hippocampus_002.nii.gz",
        "label": 1
    }
]

# Output directory
output_dir = r"c:\The Sketchbook\SEM VI\CV-Project\3d-medical-dashboard\public\models"

for task in tasks:
    if os.path.exists(task["path"]):
        # Export refined version (Standard)
        export_mesh(task["path"], task["label"], os.path.join(output_dir, f"{task['name'].lower()}.json"), task["name"], apply_morphology=True)
        
        # ALSO export a RAW version for the Spleen for comparison
        if task["name"] == "Spleen":
             export_mesh(task["path"], task["label"], os.path.join(output_dir, f"spleen_raw.json"), task["name"], apply_morphology=False)
    else:
        print(f"Path not found: {task['path']}")
