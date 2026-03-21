import re

filepath = r'c:\Users\jeyan\Downloads\original\original\blog-details2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

META_REPLACEMENT = """    <title>Exotic & Imported Fruits in Thoothukudi | Pasumai Palangal Guide</title>
    <meta name="description" content="Discover the best Avocado, Kiwi, Washington Apples, and Seasonal Mangoes at Pasumai Palangal. The #1 premium fruits shop in Thoothukudi for retail and wholesale.">
    <meta name="keywords" content="fruit shop in Thoothukudi, premium fruits shop in Thoothukudi, imported fruits shop in Thoothukudi, fruit gift shop in Thoothukudi, kiwi fruits shop in Thoothukudi, wholesale fruits in Thoothukudi.">"""

html = re.sub(r'<title>.*?</title>', META_REPLACEMENT, html, flags=re.DOTALL)

NEW_BLOG_CONTENT = """                <div class="container-sm">
                    <div class="row justify-content-center">
                        <div class="col-md-9">
                            <div class="blog_details_cont">
                                <span class="blog_date">Pasumai Palangal | Thoothukudi | 5 min read</span>
                                <h2 class="blog_title text-capitalize">The Ultimate Guide to Premium Fruits in Thoothukudi: From Local Favourites to Exotic Imports</h2>
                                <div class="blog_author_cont d-flex align-items-center py-3">
                                    <span class="author_name me-5"><font>Posted by</font> Pasumai Palangal</span>
                                    <span class="author_position me-5"><font>In:</font> Premium Fruits</span>
                                    <span class="author_comment"><font>Comments:</font> 0</span>
                                </div>
                                <p class="blog_desc py-3">Walking into a fruit shop in Thoothukudi used to mean choosing between a few local varieties. But at Pasumai Palangal, we've changed the game. Whether you are looking for daily nutrition or a high-end corporate gift in Thoothukudi, your choices just got a lot more interesting.</p>

                                <p class="blog_desc py-3">Here is a breakdown of the four tiers of fruit excellence available at our premium fruits shop in Thoothukudi.</p>
                                
                                <h3 class="blog_section_title pt-4">1. The Trendsetters: Exotic Fruits</h3>
                                <p class="blog_desc py-3">If you see it on a health influencer's plate, it's probably in our <strong>exotic fruits</strong> section. These are for the high-performers and the health-conscious elite.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>Avocado & Dragon Fruit:</strong> The kings of healthy fats and antioxidants.</li>
                                        <li><i class="fas fa-check"></i> <strong>Blueberries & Kiwi:</strong> Essential for anyone searching for a kiwi fruit shop in Thoothukudi that actually stocks fresh, Zespri-grade quality.</li>
                                        <li><i class="fas fa-check"></i> <strong>Passion Fruit:</strong> The aromatic powerhouse perfect for high-end cafe fruits in Thoothukudi, nearby.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">2. The Global Standards: Imported Fruits</h3>
                                <p class="blog_desc py-3">Why settle for mediocre when you can have the world's best? Our imported fruits shop in Thoothukudi brings the orchard to your doorstep.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>Washington & Green Apples:</strong> Crisp, reliable, and far superior to local cold-storage stock.</li>
                                        <li><i class="fas fa-check"></i> <strong>Red Globe Grapes & Pears:</strong> Sweetness and texture that you simply can't find at a standard nearby fruit shop in Thoothukudi.</li>
                                        <li><i class="fas fa-check"></i> <strong>Mandarin Oranges:</strong> The perfect snack for children, easy to peel and packed with Vitamin C.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">3. The Rare Finds: Seasonal Specialities</h3>
                                <p class="blog_desc py-3">Immunity and health are tied to the seasons. We track the harvest calendar so you don't have to.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>The Big Three:</strong> Mangosteen, Rambutan, and Mangoes (Alphonso/Imampasand).</li>
                                        <li><i class="fas fa-check"></i> <strong>The Treats:</strong> Fresh Cherries and Plums.</li>
                                        <li><i class="fas fa-check"></i> <em>Note:</em> These move fast. If you're looking for a unique fruit gift shop in Thoothukudi, our seasonal hampers are the most "Instagrammable" gift you can send.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">4. The Daily Essentials: Fresh Tropical Fruits</h3>
                                <p class="blog_desc py-3">Just because it's local doesn't mean it should be basic. Our tropical selection is sourced for maximum freshness and zero chemical ripening.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>Bananas & Papaya:</strong> The backbone of the South Indian diet.</li>
                                        <li><i class="fas fa-check"></i> <strong>Pineapple & Guava:</strong> Naturally ripened and ready for your morning bowl or a fresh glass at a juice shop in Thoothukudi.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">Which Category Fits Your Goal?</h3>
                                <div class="table-responsive pt-3">
                                    <table class="table table-bordered">
                                        <thead class="bg-light">
                                            <tr>
                                                <th>Your Goal</th>
                                                <th>Recommended Category</th>
                                                <th>Key Fruit</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><strong>Weight Loss/Keto</strong></td>
                                                <td>Exotic</td>
                                                <td>Avocado</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Child's Health</strong></td>
                                                <td>Imported</td>
                                                <td>Washington Apple</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Managing Diabetes</strong></td>
                                                <td>Exotic</td>
                                                <td>Blueberries / Kiwi</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Traditional Gifting</strong></td>
                                                <td>Seasonal</td>
                                                <td>Alphonso Mangoes</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>

                                <h3 class="blog_section_title pt-4">Why Thoothukudi Trusts Pasumai Palangal</h3>
                                <p class="blog_desc py-3">We don't just sell fruit; we manage a supply chain. From wholesale fruits in Thoothukudi for local businesses to individual retail boxes, every piece of fruit is inspected for "retail-grade" perfection.</p>
                                <p class="blog_desc py-3">Don't gamble with your health at a random roadside stall. Visit Pasumai Palangal in Thoothukudi, the only place where global quality meets local trust.</p>

                            </div>
                        </div>
                    </div>
                </div>"""

# Replace content between <section class="blog_details...> and <hr>
html = re.sub(r'(<section class="blog_details[^>]*>).*?(<hr>)', r'\1\n' + NEW_BLOG_CONTENT + r'\n                    \2', html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
