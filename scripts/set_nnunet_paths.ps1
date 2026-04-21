param(
  [switch]$PersistUser
)

# PowerShell requires param(...) to be the first executable statement.
$ErrorActionPreference = "Stop"

# Usage:
#   .\scripts\set_nnunet_paths.ps1
#   .\scripts\set_nnunet_paths.ps1 -PersistUser
#
# This sets nnU-Net v2 environment variables so it can find raw/preprocessed/results folders.

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

$raw = Resolve-Path (Join-Path $repoRoot "nnUNet\\data\\nnUNet_raw")
$preprocessed = Resolve-Path (Join-Path $repoRoot "nnUNet\\data\\nnUNet_preprocessed")
$results = Resolve-Path (Join-Path $repoRoot "nnUNet\\data\\nnUNet_results")

$env:nnUNet_raw = $raw.Path
$env:nnUNet_preprocessed = $preprocessed.Path
$env:nnUNet_results = $results.Path

Write-Host "Set nnU-Net paths for this session:"
Write-Host "  nnUNet_raw=$($env:nnUNet_raw)"
Write-Host "  nnUNet_preprocessed=$($env:nnUNet_preprocessed)"
Write-Host "  nnUNet_results=$($env:nnUNet_results)"

if ($PersistUser) {
  [Environment]::SetEnvironmentVariable("nnUNet_raw", $env:nnUNet_raw, "User")
  [Environment]::SetEnvironmentVariable("nnUNet_preprocessed", $env:nnUNet_preprocessed, "User")
  [Environment]::SetEnvironmentVariable("nnUNet_results", $env:nnUNet_results, "User")
  Write-Host "Persisted nnU-Net paths to User environment variables."
}
