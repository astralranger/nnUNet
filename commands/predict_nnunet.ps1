$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

$input_folder = "C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw\Dataset002_Heart\imagesTs"
$output_folder = "C:\The Sketchbook\SEM VI\CV-Project\data\predictions"

If (!(Test-Path $output_folder)) {
    New-Item -ItemType Directory -Path $output_folder
}

Write-Host "Predicting segmentations for test images using checkpoint_best.pth..."
.\venv\Scripts\nnUNetv2_predict.exe -i $input_folder -o $output_folder -d 2 -c 3d_fullres -f 0 -chk checkpoint_best.pth
