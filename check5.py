lines = open('index.html', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if 'pills-beverages-tab' in line or 'pills-babies-tab' in line or 'pills-frozen-tab' in line:
        print(f'{i+1}: {lines[i].rstrip()}')
