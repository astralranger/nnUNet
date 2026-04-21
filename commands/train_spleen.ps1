$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

Write-Host "Starting nnU-Net training for Dataset 9 (Spleen), Configuration: 3d_fullres, Fold: 0..."
.\venv\Scripts\nnUNetv2_train.exe 9 3d_fullres 0
