lines = open('assets/css/style.css', encoding='utf-8').readlines()
for i in range(2298, 2325):
    print(f'{i+1}: {lines[i].rstrip()}')
