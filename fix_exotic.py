fruits = [
    ("Gala Apple",          "assets/images/product/product35.png"),
    ("Green Apple",         "assets/images/product/greenapple.png"),
    ("Golden Kiwi",         "assets/images/product/golden kiwi.png"),
    ("Green Kiwi",          "assets/images/product/greenkiwi.png"),
    ("Blueberry",           "assets/images/product/blueberry.png"),
    ("Red Cherry",          "assets/images/product/redcherry.png"),
    ("Longan",              "assets/images/product/longan.png"),
    ("Mandarin Orange",     "assets/images/product/mandarinorange.webp"),
    ("Avocado",             "assets/images/product/avacado.png"),
    ("Red Dragon Fruit",    "assets/images/product/reddragon.png"),
    ("White Dragon Fruit",  "assets/images/product/whitedragon.webp"),
    ("Strawberry",          "assets/images/product/strawberry.webp"),
    ("Grapefruit",          "assets/images/product/grapefruit.webp"),
    ("Muscat Shine Grapes", "assets/images/product/hills-banana.webp"),
    ("Persimmon",           "assets/images/product/persimmon.webp"),
]

def card(name, img):
    return f'''                                        <div class="col-md-6">
                                           <div class="prdc_ctg_product_content d-flex justify-content-center align-items-center">
                                              <div class="prdc_ctg_product_img d-flex justify-content-center align-items-center me-3">
                                                 <img src="{img}" alt="{name}" style="width:70px;height:70px;object-fit:contain;">
                                              </div>
                                              <div class="prdc_ctg_product_text">
                                                 <div class="prdc_ctg_product_badge mb-2">
                                                    <span class="text-uppercase rounded-pill">Exotic</span>
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

pages = [fruits[0:6], fruits[6:12], fruits[12:15]]

pages_html = ""
for p_idx, page in enumerate(pages):
    active = "show active" if p_idx == 0 else ""
    cards_html = "\n".join(card(n, i) for n, i in page)
    pages_html += f'''                                  <div class="exotic-page" id="exotic-page-{p_idx+1}" style="{'display:block' if p_idx==0 else 'display:none'}">
                                     <div class="row">
{cards_html}
                                     </div>
                                  </div>
'''

pagination_html = '''                                  <div class="exotic-pagination d-flex justify-content-center align-items-center mt-3 gap-2">
                                     <button class="btn btn-sm exotic-prev-btn" onclick="exoticPage(-1)" style="background-color:#e66c08;color:white;border-radius:50%;width:32px;height:32px;padding:0;"><i class="fas fa-chevron-left"></i></button>
                                     <span class="exotic-page-num" id="exotic-page-indicator" style="font-weight:600;color:#333;">1 / 3</span>
                                     <button class="btn btn-sm exotic-next-btn" onclick="exoticPage(1)" style="background-color:#e66c08;color:white;border-radius:50%;width:32px;height:32px;padding:0;"><i class="fas fa-chevron-right"></i></button>
                                  </div>
                                  <script>
                                  (function(){
                                     var cur = 1, total = 3;
                                     window.exoticPage = function(dir){
                                        var next = cur + dir;
                                        if(next < 1 || next > total) return;
                                        document.getElementById('exotic-page-' + cur).style.display = 'none';
                                        cur = next;
                                        document.getElementById('exotic-page-' + cur).style.display = 'block';
                                        document.getElementById('exotic-page-indicator').textContent = cur + ' / ' + total;
                                     };
                                  })();
                                  </script>'''

new_section = f'''                            <div class="tab-pane fade show active" id="pills-beverages" role="tabpanel" aria-labelledby="pills-beverages-tab">
                               <div class="prdc_ctg_product_wrap">
                                  <div class="prdc_ctg_inner_product bg-white">
{pages_html}{pagination_html}
                                  </div>
                               </div>
                            </div>'''

content = open('index.html', encoding='utf-8').read()

# Find and replace the pills-beverages tab-pane block
import re
pattern = r'<div class="tab-pane fade" id="pills-beverages".*?</div>\s*</div>\s*</div>\s*</div>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_section + content[match.end():]
    open('index.html', 'w', encoding='utf-8').write(content)
    print(f"Replaced at char {match.start()} - {match.end()}")
else:
    print("Pattern not found")
