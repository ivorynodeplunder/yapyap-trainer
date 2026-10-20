param(
    [string]$OutDir = "dist"
)
$ErrorActionPreference = "Stop"
Write-Host "[yapyap] building single-file exe..."
pyinstaller --noconfirm --onefile --name yapyap-trainer `
    --add-data "config;config" `
    --hidden-import pymem `
    src/bootstrap/main.py
Move-Item -Force "dist/yapyap-trainer.exe" "$OutDir/yapyap-trainer.exe"
Write-Host "[yapyap] done -> $OutDir/yapyap-trainer.exe"