lines = open('index.html', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if 'pills-beverages' in line and 'tab-pane' in line:
        for j in range(i, i+10):
            print(f'{j+1}: {lines[j].rstrip()}')
        print('...')
        # find exotic-page divs
    if 'exotic-page' in line:
        print(f'{i+1}: {lines[i].rstrip()}')
    if 'exotic-pagination' in line:
        print(f'{i+1}: {lines[i].rstrip()}')
    if 'exoticPage' in line and 'script' not in line.lower():
        print(f'{i+1}: {lines[i].rstrip()}')
