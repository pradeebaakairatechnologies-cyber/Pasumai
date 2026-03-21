content = open('index.html', encoding='utf-8').read()

# Find exact positions using line-based search
lines = content.split('\n')

pills_fruits_line = None
pills_fresh_line = None
pills_beverages_line = None
pills_babies_line = None

for i, line in enumerate(lines):
    if 'tab-pane' in line:
        if 'id="pills-fruits"' in line and pills_fruits_line is None:
            # Only the one inside produce_category_section (col-xl-8)
            # Check context - it should be preceded by tab-content
            if i > 2300 and i < 2400:
                pills_fruits_line = i
        if 'id="pills-fresh"' in line:
            pills_fresh_line = i
        if 'id="pills-beverages"' in line and pills_beverages_line is None:
            pills_beverages_line = i
        if 'id="pills-babies"' in line and pills_babies_line is None:
            pills_babies_line = i

print(f"pills-fruits: {pills_fruits_line+1 if pills_fruits_line else None}")
print(f"pills-fresh: {pills_fresh_line+1 if pills_fresh_line else None}")
print(f"pills-beverages: {pills_beverages_line+1 if pills_beverages_line else None}")
print(f"pills-babies: {pills_babies_line+1 if pills_babies_line else None}")

# Remove lines from pills-fruits start to pills-beverages start (exclusive)
# Also fix indentation of pills-beverages opening line
new_lines = lines[:pills_fruits_line]  # everything before pills-fruits

# Fix the pills-beverages opening line indentation to match pills-babies (27 spaces)
bev_line = lines[pills_beverages_line]
# Replace the excessive leading spaces with correct 27 spaces
correct_indent = '                           '  # 27 spaces like pills-babies
bev_line_fixed = correct_indent + bev_line.lstrip()
lines[pills_beverages_line] = bev_line_fixed

# Add from pills-beverages onward
new_lines += lines[pills_beverages_line:]

open('index.html', 'w', encoding='utf-8').write('\n'.join(new_lines))
print("Done")

# Verify
result = open('index.html', encoding='utf-8').read().split('\n')
for i, line in enumerate(result):
    if 'tab-pane' in line and any(x in line for x in ['pills-fruits','pills-fresh','pills-beverages','pills-babies','pills-frozen']):
        print(f'{i+1}: {line.rstrip()}')
