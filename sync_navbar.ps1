$indexLines = Get-Content 'index.html'

# Extract header from index.html (between <!-- header section start --> and </header>)
$headerStart = $null; $headerEnd = $null
for ($i = 0; $i -lt $indexLines.Length; $i++) {
    if ($indexLines[$i] -match '<!-- header section start -->') { $headerStart = $i }
    if ($indexLines[$i] -match '</header>' -and $headerStart -ne $null) { $headerEnd = $i; break }
}
$newHeader = $indexLines[$headerStart..$headerEnd] -join "`n"

$pages = @('about-us.html','blog-details.html','blog-list.html','compare.html','contact-us.html','faqs.html','product-detail.html')

foreach ($page in $pages) {
    $lines = Get-Content $page
    $start = $null; $end = $null
    for ($i = 0; $i -lt $lines.Length; $i++) {
        if ($lines[$i] -match '<!-- header section start -->') { $start = $i }
        if ($lines[$i] -match '</header>' -and $start -ne $null) { $end = $i; break }
    }
    if ($start -eq $null -or $end -eq $null) { Write-Output "SKIP: $page (header not found)"; continue }

    $before = $lines[0..($start-1)] -join "`n"
    $after  = $lines[($end+1)..($lines.Length-1)] -join "`n"
    $result = $before + "`n" + $newHeader + "`n" + $after
    Set-Content $page $result -NoNewline
    Write-Output "Updated: $page"
}
