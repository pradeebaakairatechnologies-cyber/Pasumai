import re

filepath = r'c:\Users\jeyan\Downloads\original\original\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of style="width:70px;height:70px;object-fit:contain;"
# with style="width:100%;height:100%;object-fit:cover;border-radius:50%;"
new_content = re.sub(
    r'style="width:\s*70px\s*;\s*height:\s*70px\s*;\s*object-fit:\s*contain\s*;"',
    r'style="width:100%;height:100%;object-fit:cover;border-radius:50%;"',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement complete.")
