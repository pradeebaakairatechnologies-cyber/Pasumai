$pages = @('index.html','about-us.html','blog-details.html','blog-list.html','compare.html','contact-us.html','faqs.html','product-detail.html')

foreach ($page in $pages) {
    $content = Get-Content $page -Raw

    # Fix the li: remove "dropdown" class
    $content = $content -replace '<li class="nav-item nav_item_has_child px-2 dropdown">', '<li class="nav-item nav_item_has_child px-2">'

    # Fix the a: remove Bootstrap dropdown attributes
    $content = $content -replace '<a class="nav-link" href="#" id="blog_submenu" role="button" data-bs-toggle="dropdown" aria-expanded="false">Blog</a>', '<a class="nav-link" href="#">Blog</a>'

    # Fix the div: remove "dropdown-menu" class and aria attribute
    $content = $content -replace '<div class="nav_item_submenu dropdown-menu" aria-labelledby="blog_submenu"', '<div class="nav_item_submenu"'

    Set-Content $page $content -NoNewline
    Write-Output "Updated: $page"
}
