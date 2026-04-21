$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

Write-Host "Starting short nnU-Net training (50 epochs) for Dataset 2 (Heart)..."
# Using -tr to specify the number of epochs (some versions allow this) 
# or setting it via a higher-level command if supported.
# Since nnUNet v2 strict training is hardcoded to 1000, 
# we can use a custom trainer or just monitor it.
# However, many people use -tr nnUNetTrainer_50epochs if it exists, or just override.

.\venv\Scripts\nnUNetv2_train.exe 2 3d_fullres 0 --num_epochs 50
