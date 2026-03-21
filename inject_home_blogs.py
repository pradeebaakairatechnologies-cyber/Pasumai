import re

filepath = r'c:\Users\jeyan\Downloads\original\original\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

NEW_HTML = """                     <div class="col-md-6 col-lg-4">
                        <div class="gallery_mid_content overflow-hidden bg-white shadow-lg">
                           <div class="gallery_mid_thumb">
                              <img src="assets/images/blog/blog7.png" alt="5 Benefits of Eating Organic fruitss Daily">
                           </div>
                           <div class="gallery_mid_inner_content px-5 py-4">
                              <a href="blog-details.html">
                                 <h2>5 Benefits of Eating Organic fruitss Daily</h2>
                              </a>
                              <div class="gallery_mid_author_content py-2 d-flex justify-content-between">
                                 <div class="gallery_mid_author_title">
                                    <span><i class="far fa-user pe-1"></i> Priya Nair</span>
                                 </div>
                                 <div class="gallery_mid_author_time">
                                    <span><i class="far fa-clock pe-1"></i> 6 hours ago</span>
                                 </div>
                              </div>
                              <div class="gallery_mid_desc">
                                 <p>Switching to organic produce can improve your health, reduce pesticide exposure, and support local Tamil Nadu farmers who use sustainable methods.</p>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-6 col-lg-4">
                        <div class="gallery_end_content px-4 py-5 overflow-auto bg-white">
                           <div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">
                              <div class="gallery_end_thumb me-3">
                                 <img src="assets/images/blog/blog8.png" alt="Strawberries vs. Raspberries" style="width:100px; height:100px; object-fit:cover; border-radius:10px;">
                              </div>
                              <div class="gallery_end_inner_content">
                                 <a href="blog-details1.html">
                                    <h4 style="font-size:16px; line-height:1.4;">Strawberries vs. Raspberries: Which Is Better for You?</h4>
                                 </a>
                                 <div class="gallery_end_author_content d-flex">
                                    <div class="gallery_end_author_title pe-2">
                                       <span><i class="far fa-user pe-1"></i> Anand Rajan</span>
                                    </div>
                                    <div class="gallery_end_author_time">
                                       <span><i class="far fa-clock pe-1"></i> 1 day ago</span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">
                              <div class="gallery_end_thumb me-3">
                                 <img src="assets/images/sales/sale1.png" alt="Ultimate Guide to Premium Fruits" style="width:100px; height:100px; object-fit:cover; border-radius:10px;">
                              </div>
                              <div class="gallery_end_inner_content">
                                 <a href="blog-details2.html">
                                    <h4 style="font-size:16px; line-height:1.4;">The Ultimate Guide to Premium Fruits in Thoothukudi</h4>
                                 </a>
                                 <div class="gallery_end_author_content d-flex">
                                    <div class="gallery_end_author_title pe-2">
                                       <span><i class="far fa-user pe-1"></i> Meena Sub.</span>
                                    </div>
                                    <div class="gallery_end_author_time">
                                       <span><i class="far fa-clock pe-1"></i> 2 days ago</span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="gallery_end_content_item mb-5 d-flex justify-content-center align-items-center">
                              <div class="gallery_end_thumb me-3">
                                 <img src="assets/images/grid/grid1.png" alt="Traditional Tamil Recipes" style="width:100px; height:100px; object-fit:cover; border-radius:10px;">
                              </div>
                              <div class="gallery_end_inner_content">
                                 <a href="blog-details.html">
                                    <h4 style="font-size:16px; line-height:1.4;">Traditional Tamil Recipes with Organic Ingredients</h4>
                                 </a>
                                 <div class="gallery_end_author_content d-flex">
                                    <div class="gallery_end_author_title pe-2">
                                       <span><i class="far fa-user pe-1"></i> Kavitha Mur.</span>
                                    </div>
                                    <div class="gallery_end_author_time">
                                       <span><i class="far fa-clock pe-1"></i> 3 days ago</span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="gallery_end_content_item d-flex justify-content-center align-items-center">
                              <div class="gallery_end_thumb me-3">
                                 <img src="assets/images/blog/blog9.png" alt="Organic Certification" style="width:100px; height:100px; object-fit:cover; border-radius:10px;">
                              </div>
                              <div class="gallery_end_inner_content">
                                 <a href="blog-details.html">
                                    <h4 style="font-size:16px; line-height:1.4;">Why Organic Certification Matters for Consumers</h4>
                                 </a>
                                 <div class="gallery_end_author_content d-flex">
                                    <div class="gallery_end_author_title pe-2">
                                       <span><i class="far fa-user pe-1"></i> Dr. Selvam Pillai</span>
                                    </div>
                                    <div class="gallery_end_author_time">
                                       <span><i class="far fa-clock pe-1"></i> 4 days ago</span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>"""

pattern = r'(<div class="col-md-6 col-lg-4">\s*<div class="gallery_mid_content overflow-hidden bg-white shadow-lg">.*?)(?=\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>)'

html = re.sub(pattern, NEW_HTML, html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
