$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

Write-Host "Converting Task05_Prostate (MSD format) to Dataset005_Prostate (nnUNetv2 format)..."
.\venv\Scripts\nnUNetv2_convert_MSD_dataset.exe -i "C:\The Sketchbook\SEM VI\CV-Project\Task05_Prostate\Task05_Prostate" -overwrite_id 5

Write-Host "Fingerprinting and Preprocessing Dataset005_Prostate..."
.\venv\Scripts\nnUNetv2_plan_and_preprocess.exe -d 5 --verify_dataset_integrity
