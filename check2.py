lines = open('index.html', encoding='utf-8').readlines()
for i in range(844, 875):
    print(f'{i+1}: {lines[i].rstrip()}')
