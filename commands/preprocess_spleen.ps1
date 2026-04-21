$env:nnUNet_raw="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_raw"
$env:nnUNet_preprocessed="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_preprocessed"
$env:nnUNet_results="C:\The Sketchbook\SEM VI\CV-Project\data\nnUNet_results"

Write-Host "Converting Task09_Spleen (MSD format) to Dataset009_Spleen (nnUNetv2 format)..."
.\venv\Scripts\nnUNetv2_convert_MSD_dataset.exe -i "C:\The Sketchbook\SEM VI\CV-Project\Task09_Spleen\Task09_Spleen" -overwrite_id 9

Write-Host "Fingerprinting and Preprocessing Dataset009_Spleen (CT scans)..."
.\venv\Scripts\nnUNetv2_plan_and_preprocess.exe -d 9 --verify_dataset_integrity
