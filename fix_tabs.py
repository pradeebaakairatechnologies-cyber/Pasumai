def make_card(img, alt, name):
    return f'''                        <div class="col-sm-6 col-md-6 col-xl-3">
                           <div class="product_layout_1 overflow-hidden position-relative">
                              <div class="product_layout_content bg-white position-relative">
                                 <div class="product_image_wrap">
                                    <a class="product_image d-flex justify-content-center align-items-center" href="shop-list.html" target="_blank">
                                       <img class="pic-1" src="assets/images/product/{img}" alt="{alt}">
                                       <img class="pic-2" src="assets/images/product/{img}" alt="{alt}">
                                    </a>
                                    <ul class="product_badge_group ul_li_block">
                                       <li><span class="product_badge badge_meats position-absolute rounded-pill text-uppercase">Meats</span>
                                       </li>
                                       </li>
                                    </ul>
                                    <ul class="product_action_btns ul_li_block d-flex">
                                       <li><a class="tooltips" data-placement="top" title="Search Product" href="index.html"><i class="fas fa-search"></i></a></li>
                                    </ul>
                                 </div>
                                 <div class="rating_wrap d-flex">
                                    <ul class="rating_star ul_li">
                                       <li class="active"><i class="fas fa-star"></i></li>
                                       <li class="active"><i class="fas fa-star"></i></li>
                                       <li class="active"><i class="fas fa-star"></i></li>
                                       <li class="active"><i class="fas fa-star"></i></li>
                                       <li><i class="far fa-star"></i></li>
                                    </ul>
                                    <span class="shop_review_text">( 4.0 )</span>
                                 </div>
                                 <div class="product_content">
                                    <h3 class="product_title">
                                       <a href="shop-list.html" target="_blank">{name}</a>
                                    </h3>
                                    <div class="product_price">
                                      
                                       
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>'''

exotic = [
    ("gala-apple.png", "Gala Apple", "Gala Apple"),
    ("greenapple.png", "Green Apple", "Green Apple"),
    ("golden kiwi.png", "Golden Kiwi", "Golden Kiwi"),
    ("greenkiwi.png", "Green Kiwi", "Green Kiwi"),
    ("blueberry.png", "Blueberry", "Blueberry"),
    ("redcherry.png", "Red Cherry", "Red Cherry"),
    ("longan.png", "Longan", "Longan"),
    ("mandarinorange.webp", "Mandarin Orange", "Mandarin Orange"),
]

tropical = [
    ("Mango - Immampasanth.png", "Mango Imampasand", "Mango Imampasand"),
    ("mango-alphonsa.webp", "Mango Alphonsa", "Mango Alphonsa"),
    ("mangosteen.webp", "Mangosteen", "Mangosteen"),
    ("p16.jpg", "Rambutan", "Rambutan"),
    ("durian.webp", "Durian", "Durian"),
    ("lychee.webp", "Lychee", "Lychee"),
    ("passion-fruit.webp", "Passion Fruit", "Passion Fruit"),
    ("hills-banana.webp", "Hill Banana", "Hill Banana"),
]

def make_tab(items):
    cards = '\n'.join(make_card(*i) for i in items)
    return f'''                  <div class="row g-4">
{cards}
                     </div>'''

with open('index.html', encoding='utf-8') as f:
    content = f.read()

import re

# Replace pills-fruits tab content
exotic_tab_new = f'<div class="tab-pane fade" id="pills-fruits" role="tabpanel" aria-labelledby="pills-fruits-tab">\n                     {make_tab(exotic)}\n                  </div>'
content = re.sub(
    r'<div class="tab-pane fade" id="pills-fruits".*?</div>\s*</div>\s*</div>',
    exotic_tab_new,
    content, count=1, flags=re.DOTALL
)

# Replace pills-bread tab content
tropical_tab_new = f'<div class="tab-pane fade" id="pills-bread" role="tabpanel" aria-labelledby="pills-bread-tab">\n                     {make_tab(tropical)}\n                  </div>'
content = re.sub(
    r'<div class="tab-pane fade" id="pills-bread".*?</div>\s*</div>\s*</div>',
    tropical_tab_new,
    content, count=1, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
