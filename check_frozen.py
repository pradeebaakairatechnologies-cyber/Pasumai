content = open('index.html', encoding='utf-8').read()
start = content.find('id="pills-frozen"')
print(repr(content[start:start+3000]))
