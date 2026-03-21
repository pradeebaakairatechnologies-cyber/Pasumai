lines = open('index.html', encoding='utf-8').readlines()
print("=== Lines 2313-2330 ===")
for i in range(2312, 2330):
    print(f'{i+1}: {lines[i].rstrip()}')
