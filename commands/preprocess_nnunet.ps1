$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

New-Item -ItemType Directory -Force -Path $env:nnUNet_raw
New-Item -ItemType Directory -Force -Path $env:nnUNet_preprocessed
New-Item -ItemType Directory -Force -Path $env:nnUNet_results

Write-Host "Converting MSD dataset to nnUNetv2 format..."
.\venv\Scripts\nnUNetv2_convert_MSD_dataset.exe -i "C:\The Sketchbook\SEM VI\CV-Project\Task02_Heart\Task02_Heart"

Write-Host "Fingerprinting and Preprocessing (this will take time)..."
.\venv\Scripts\nnUNetv2_plan_and_preprocess.exe -d 2 --verify_dataset_integrity
