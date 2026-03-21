import re
content = open('index.html', encoding='utf-8').read()
start = content.find('testimonial section start')
end = content.find('testimonial section end')
section = content[start:end]
names = re.findall(r'<h6>([^<]+)</h6>', section)
print(names)
