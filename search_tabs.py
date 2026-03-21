keywords = ['pills-all','pills-babies','pills-frozen','pills-beverages','nav-link','Exotic','Tropical','Seasonal','Stone Fruits','All Fruits','Fresh Juices','organic','tab']
with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines, 1):
    if any(x in l for x in keywords):
        print(i, l.rstrip())
