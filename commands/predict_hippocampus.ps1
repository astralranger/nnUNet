$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

$input_folder = "C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset004_Hippocampus\imagesTs"
$output_folder = "C:\The Sketchbook\SEM VI\CV-Project\data\predictions_hippocampus"

If (!(Test-Path $output_folder)) {
    New-Item -ItemType Directory -Path $output_folder
}

Write-Host "Predicting Hippocampus regions (3D Fullres) using best checkpoint..."
.\venv\Scripts\nnUNetv2_predict.exe -i $input_folder -o $output_folder -d 4 -c 3d_fullres -f 0 -chk checkpoint_best.pth
