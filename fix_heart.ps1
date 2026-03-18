$file = "index.html"
$content = Get-Content $file -Raw
$content = $content -replace '(?m)^\s*<li class="pe-2"><a href="cart\.html"><i class="far fa-heart"></i></a></li>\r?\n', ''
Set-Content $file $content -NoNewline
