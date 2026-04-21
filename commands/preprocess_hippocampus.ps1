$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

Write-Host "Converting Task04_Hippocampus (MSD format) to Dataset004_Hippocampus (nnUNetv2 format)..."
.\venv\Scripts\nnUNetv2_convert_MSD_dataset.exe -i "C:\The Sketchbook\SEM VI\CV-Project\Task04_Hippocampus\Task04_Hippocampus" -overwrite_id 4

Write-Host "Fingerprinting and Preprocessing Dataset004_Hippocampus..."
.\venv\Scripts\nnUNetv2_plan_and_preprocess.exe -d 4 --verify_dataset_integrity
