import re
import glob

# 1. Update index.html
index_path = r'c:\Users\jeyan\Downloads\original\original\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the gallery_mid_author_content block
html = re.sub(r'<div class="gallery_mid_author_content.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)
# Remove the gallery_end_author_content block
html = re.sub(r'<div class="gallery_end_author_content.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {index_path}")

# 2. Update blog-list.html
blog_list_path = r'c:\Users\jeyan\Downloads\original\original\blog-list.html'
with open(blog_list_path, 'r', encoding='utf-8') as f:
    html = f.read()

# In blog-list.html, the container is grid_author_cont containing gallery_mid_author_content
html = re.sub(r'<div class="grid_author_cont">.*?</div>\s*</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

with open(blog_list_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {blog_list_path}")
