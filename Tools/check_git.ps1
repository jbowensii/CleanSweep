Set-Location 'C:\Unreal Projects\Moria'

$gitFiles = git ls-files
Write-Host "Git tracked files: $($gitFiles.Count)"

$untracked = git ls-files --others --exclude-standard
Write-Host "Untracked files: $($untracked.Count)"

if ($untracked.Count -gt 0) {
    Write-Host "UNTRACKED:"
    $untracked
} else {
    Write-Host "All files are tracked - nothing missing!"
}

$lfsFiles = git lfs ls-files
Write-Host "LFS tracked files: $($lfsFiles.Count)"
