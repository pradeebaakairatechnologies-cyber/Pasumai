with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

name_map = {
    'gala_apple': 'Gala Apple',
    'greenapple': 'Green Apple',
    'golden kiwi': 'Golden Kiwi',
    'greenkiwi': 'Green Kiwi',
    'blueberry': 'Blueberry',
    'redcherry': 'Red Cherry',
    'longan': 'Longan',
    'mandarinorange': 'Mandarin Orange',
    'avacado': 'Avocado',
    'reddragon': 'Red Dragon Fruit',
    'whitedragon': 'White Dragon Fruit',
    'strawberry': 'Strawberry',
    'grapefruit': 'Grapefruit',
    'hills-banana': 'Hills Banana',
    'persimmon': 'Persimmon',
}

lines = content.split('\n')
last_name = None
result = []
for line in lines:
    if 'class="pic-1"' in line and 'src=' in line:
        last_name = None
        for key, val in name_map.items():
            if key in line:
                last_name = val
                # fix alt="image_not_found" -> alt="Name"
                line = line.replace('alt="image_not_found"', f'alt="{val}"')
                break
    elif 'class="pic-2"' in line and 'src=' in line and last_name:
        line = line.replace('alt="image_not_found"', f'alt="{last_name}"')
    elif 'class="product_title"' in line:
        pass  # title is on the next <a> line
    elif last_name and '>Organic Fruits<' in line and '<a ' in line:
        line = line.replace('>Organic Fruits<', f'>{last_name}<')
        last_name = None
    result.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Done')
