with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

in_fruits = False
in_bread = False
for i, l in enumerate(lines, 1):
    if 'id="pills-fruits"' in l:
        in_fruits = True
        in_bread = False
        print(f"=== pills-fruits starts line {i} ===")
    if 'id="pills-bread"' in l:
        in_bread = True
        in_fruits = False
        print(f"=== pills-bread starts line {i} ===")
    if 'id="pills-meat"' in l:
        in_bread = False
        print(f"=== pills-meat starts line {i} (end of bread) ===")
    if (in_fruits or in_bread) and ('product_title' in l or 'pic-1' in l):
        print(i, l.rstrip())
