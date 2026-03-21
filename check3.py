lines = open('index.html', encoding='utf-8').readlines()
# Find pills-beverages tab pane
for i, line in enumerate(lines):
    if 'pills-beverages' in line and 'tab-pane' in line:
        for j in range(i, i+200):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
