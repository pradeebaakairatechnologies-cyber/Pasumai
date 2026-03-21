import re
import glob

files = glob.glob(r'c:\Users\jeyan\Downloads\original\original\blog-details*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The block we want to remove starts with <hr> and ends right before </section>
    # Note that <hr> is inside `<div class="container-sm">`
    # We want to replace `<hr> ...  </div>\n            </section>` with `</div>\n            </section>`
    
    new_html = re.sub(r'<hr>\s*(<div class="row">.*?)</div>\s*</section>', r'</div>\n            </section>', html, flags=re.DOTALL)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}. Regex didn't match.")
