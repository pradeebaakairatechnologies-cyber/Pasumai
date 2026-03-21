content = open('index.html', encoding='utf-8').read()

import re

start = content.find('id="pills-babies"')
end = content.find('id="pills-frozen"')

babies_section = content[start:end]
print("=== CURRENT pills-babies images ===")
imgs = re.findall(r'<img src="([^"]+)"[^>]*alt="([^"]*)"', babies_section)
for src, alt in imgs:
    print(f"  src={src}  alt={alt}")
