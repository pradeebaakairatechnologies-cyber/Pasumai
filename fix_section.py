content = open('index.html', encoding='utf-8').read()
lines = content.split('\n')

# Find line indices (0-based)
pills_fruits_line = None
pills_fresh_line = None
pills_beverages_line = None
section_end_line = None

for i, line in enumerate(lines):
    if 'produce_category_section' in line:
        sec_start = i
    if i > 2200:
        if '<div class="tab-pane' in line and 'id="pills-fruits"' in line and pills_fruits_line is None:
            pills_fruits_line = i
        if '<div class="tab-pane' in line and 'id="pills-fresh"' in line and pills_fresh_line is None:
            pills_fresh_line = i
        if '<div class="tab-pane' in line and 'id="pills-beverages"' in line and pills_beverages_line is None:
            pills_beverages_line = i

# Find end of pills-beverages pane (the closing </div></div></div></div> sequence)
# Section ends at line 3102 (0-based: 3102)
for i, line in enumerate(lines):
    if i > 3000 and '</section>' in line:
        section_end_line = i
        break

# The tab-content closing divs are at lines 3097-3098 (0-based)
# pills-beverages ends and then we have closing divs for tab-content, col-xl-8, row, prdc_ctg_wrap, container, section
# We need to insert pills-babies and pills-frozen BEFORE the tab-content closing div

# Find the tab-content closing div after pills-beverages
# It's the </div> that closes <div class="tab-content" id="pills-tabContent">
# Looking at output: line 3098 is "                        </div>" which closes tab-content

# Let's find it: after pills-beverages, find the line that closes tab-content
# tab-content opened at line 2318 (0-based 2317) with 24 spaces indent
# its closing </div> should also have 24 spaces

tab_content_close = None
for i in range(pills_beverages_line + 1, section_end_line):
    stripped = lines[i].rstrip()
    if stripped == '                        </div>':  # 24 spaces + </div>
        tab_content_close = i
        break

print(f"pills_fruits_line: {pills_fruits_line+1}")
print(f"pills_fresh_line: {pills_fresh_line+1}")
print(f"pills_beverages_line: {pills_beverages_line+1}")
print(f"tab_content_close: {tab_content_close+1 if tab_content_close else None}")
print(f"section_end_line: {section_end_line+1}")

# Build tropical fruits card
def tropical_card(name, img, badge="Tropical"):
    return f'''                                        <div class="col-md-6">
                                           <div class="prdc_ctg_product_content d-flex justify-content-center align-items-center">
                                              <div class="prdc_ctg_product_img d-flex justify-content-center align-items-center me-3">
                                                 <img src="{img}" alt="{name}" style="width:70px;height:70px;object-fit:contain;">
                                              </div>
                                              <div class="prdc_ctg_product_text">
                                                 <div class="prdc_ctg_product_badge mb-2">
                                                    <span class="text-uppercase rounded-pill">{badge}</span>
                                                 </div>
                                                 <div class="prdc_ctg_product_rating my-1 rating_wrap d-flex">
                                                    <ul class="rating_star ul_li">
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li><i class="far fa-star"></i></li>
                                                    </ul>
                                                    <span class="shop_review_text">( 4.0 )</span>
                                                 </div>
                                                 <div class="prdc_ctg_product_title my-2">
                                                    <a href="shop-list.html" target="_blank"><h5>{name}</h5></a>
                                                 </div>
                                              </div>
                                           </div>
                                        </div>'''

tropical_fruits = [
    ("Mango - Imampasand",  "assets/images/product/p9.png"),
    ("Mango - Alphonsa",    "assets/images/product/p15.jpg"),
    ("Mangosteen",          "assets/images/product/p16.jpg"),
    ("Rambutan",            "assets/images/product/product16.png"),
    ("Durian",              "assets/images/product/product17.png"),
    ("Lychee",              "assets/images/product/product56.png"),
    ("Passion Fruit",       "assets/images/product/grapefruit.webp"),
    ("Hill Banana",         "assets/images/product/hills-banana.webp"),
]

tropical_cards = '\n'.join(tropical_card(n, img) for n, img in tropical_fruits)

pills_babies_html = f'''                            <div class="tab-pane fade" id="pills-babies" role="tabpanel" aria-labelledby="pills-babies-tab">
                               <div class="prdc_ctg_product_wrap">
                                  <div class="prdc_ctg_inner_product bg-white">
                                     <div class="row">
{tropical_cards}
                                     </div>
                                  </div>
                               </div>
                            </div>'''

pills_frozen_html = '''                            <div class="tab-pane fade" id="pills-frozen" role="tabpanel" aria-labelledby="pills-frozen-tab">
                               <div class="prdc_ctg_product_wrap">
                                  <div class="prdc_ctg_inner_product bg-white">
                                     <div class="row">
                                        <div class="col-md-6">
                                           <div class="prdc_ctg_product_content d-flex justify-content-center align-items-center">
                                              <div class="prdc_ctg_product_img d-flex justify-content-center align-items-center me-3">
                                                 <img src="assets/images/category/cat6.png" alt="Fresh Juice">
                                              </div>
                                              <div class="prdc_ctg_product_text">
                                                 <div class="prdc_ctg_product_badge mb-2">
                                                    <span class="text-uppercase rounded-pill">Juices</span>
                                                 </div>
                                                 <div class="prdc_ctg_product_rating my-1 rating_wrap d-flex">
                                                    <ul class="rating_star ul_li">
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li class="active"><i class="fas fa-star"></i></li>
                                                       <li><i class="far fa-star"></i></li>
                                                    </ul>
                                                    <span class="shop_review_text">( 4.0 )</span>
                                                 </div>
                                                 <div class="prdc_ctg_product_title my-2">
                                                    <a href="shop-list.html" target="_blank"><h5>Fresh Juices</h5></a>
                                                 </div>
                                              </div>
                                           </div>
                                        </div>
                                     </div>
                                  </div>
                               </div>
                            </div>'''

if tab_content_close:
    # Remove pills-fruits and pills-fresh (lines pills_fruits_line to pills_beverages_line-1)
    # Insert pills-babies and pills-frozen before tab_content_close
    new_lines = (
        lines[:pills_fruits_line] +
        lines[pills_beverages_line:tab_content_close] +
        [pills_babies_html, pills_frozen_html] +
        lines[tab_content_close:]
    )
    open('index.html', 'w', encoding='utf-8').write('\n'.join(new_lines))
    print("Done!")
else:
    print("Could not find tab_content_close - checking nearby lines:")
    for i in range(pills_beverages_line+550, pills_beverages_line+620):
        print(f'{i+1}: {repr(lines[i])}')
