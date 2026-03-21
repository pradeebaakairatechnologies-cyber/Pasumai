import re

filepath = r'c:\Users\jeyan\Downloads\original\original\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the gallery_end_content block and just keep the first two gallery_end_content_item divs
pattern = r'(<div class="gallery_end_content px-4 py-5 overflow-auto bg-white">.*?<div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">.*?</div>\s*</div>\s*</div>\s*)<div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">.*?<img src="assets/images/grid/grid1\.png".*?</div>\s*</div>\s*</div>\s*<div class="gallery_end_content_item d-flex justify-content-center align-items-center">.*?<img src="assets/images/blog/blog9\.png".*?</div>\s*</div>\s*</div>'

def replace(m):
    # Keep the start and the first two items (item 1 and item 2 matched as one big chunk)
    return m.group(1)

# Wait, the regex needs to be more precise:
# Let's just find the exact string for the 3rd and 4th items and replace them with empty string.

item3_start = html.find('<div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">\n                              <div class="gallery_end_thumb me-3">\n                                 <img src="assets/images/grid/grid1.png"')

if item3_start != -1:
    # We found the start of the 3rd item! We want to safely remove it and the 4th item.
    # We can just cut the string from item3_start to the end of the 4th item.
    
    # Let's find the closing tag of the 4th item.
    # The 4th item contains "assets/images/blog/blog9.png"
    item4_end_str = '</div>\n                              </div>\n                           </div>'
    
    item4_start = html.find('assets/images/blog/blog9.png', item3_start)
    if item4_start != -1:
        item4_end = html.find(item4_end_str, item4_start) + len(item4_end_str)
        
        # Now remove from item3_start to item4_end
        new_html = html[:item3_start] + html[item4_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully removed the 3rd and 4th blog items.")
    else:
        print("Could not find the 4th item.")
else:
    print("Could not find the 3rd item.")
