$file = 'assets\css\style.css'
$content = Get-Content $file -Raw
$content = $content -replace '\.body_wrap \{[\r\n\s]+overflow: hidden;', '.body_wrap {
  overflow: visible;'
Set-Content $file $content -NoNewline
Write-Output "Done"
