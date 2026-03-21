import re

# 1. Update index.html
index_path = r'c:\Users\jeyan\Downloads\original\original\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Safe regex replacement:
# Match the opening tag of gallery_mid_author_content up to its closing tag.
# Because it has two child divs, the pattern is:
html = re.sub(
    r'<div class="gallery_mid_author_content.*?>\s*<div class="gallery_mid_author_title">.*?</div>\s*<div class="gallery_mid_author_time">.*?</div>\s*</div>',
    '', html, flags=re.DOTALL
)

html = re.sub(
    r'<div class="gallery_end_author_content.*?>\s*<div class="gallery_end_author_title.*?>.*?</div>\s*<div class="gallery_end_author_time">.*?</div>\s*</div>',
    '', html, flags=re.DOTALL
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {index_path}")

# 2. Update blog-list.html
blog_list_path = r'c:\Users\jeyan\Downloads\original\original\blog-list.html'
with open(blog_list_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<div class="grid_author_cont">\s*<div class="gallery_mid_author_content.*?>\s*<div class="gallery_mid_author_title.*?>.*?</div>\s*<div class="gallery_mid_author_time">.*?</div>\s*</div>\s*</div>',
    '', html, flags=re.DOTALL
)

with open(blog_list_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {blog_list_path}")
