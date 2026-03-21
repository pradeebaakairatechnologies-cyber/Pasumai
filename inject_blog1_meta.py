import re

filepath = r'c:\Users\jeyan\Downloads\original\original\blog-details.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

META_REPLACEMENT = """    <title>Premium Imported Fruits Shop in Thoothukudi | Pasumai Palangal</title>
    <meta name="description" content="Pasumai Palangal is Thoothukudi's trusted imported fruits shop in Chidambara Nagar. We offer fresh & premium exotic fruits for retail, wholesale & corporate gifting.">
    <meta name="keywords" content="Pasumai Palangal, Thoothukudi Brand, Imported fruits shop in Thoothukudi, Premium fruits shop in Thoothukudi, Fruit shop in Thoothukudi, Fruit wholesaler in Thoothukudi">"""

html = re.sub(r'<title>.*?</title>', META_REPLACEMENT, html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
