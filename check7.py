lines = open('index.html', encoding='utf-8').readlines()
in_section = False
for i, line in enumerate(lines):
    if 'produce_category_section' in line:
        in_section = True
    if in_section and '</section>' in line:
        print(f"Section ends: {i+1}")
        break
    if in_section and 'tab-pane' in line:
        print(f'{i+1}: {line.strip()}')
