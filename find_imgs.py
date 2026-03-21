import re
content = open('index.html', encoding='utf-8').read()
for pat in ['p9.png', 'product35.png', 'Mango', 'gala-apple']:
    matches = [(m.start(), content[max(0,m.start()-20):m.end()+20]) for m in re.finditer(pat, content)]
    print(f"=== {pat} ({len(matches)} matches) ===")
    for pos, ctx in matches:
        print(f"  line ~{content[:pos].count(chr(10))+1}: {repr(ctx)}")
