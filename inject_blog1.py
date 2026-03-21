import re

filepath = r'c:\Users\jeyan\Downloads\original\original\blog-details1.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

META_REPLACEMENT = """    <title>Strawberry vs. Raspberry: Best Fruit Shop in Thoothukudi | Pasumai Palangal</title>
    <meta name="description" content="Searching for a premium fruit shop in Thoothukudi? Compare strawberries vs. raspberries for health, blood sugar, and immunity. Visit Pasumai Palangal in Thoothukudi.">
    <meta name="keywords" content="fruit shop in Thoothukudi, Premium fruits shop in Thoothukudi, imported fruits shop in Thoothukudi, Pasumai Palangal in Thoothukudi, fruit gift shop in Thoothukudi, corporate gift in Thoothukudi, Wholesale fruits in Thoothukudi, juice shop in Thoothukudi, nearby fruit shop in Thoothukudi, kiwi fruit shop in Thoothukudi.">"""

html = re.sub(r'<title>.*?</title>', META_REPLACEMENT, html, flags=re.DOTALL)

NEW_BLOG_CONTENT = """                <div class="container-sm">
                    <div class="row justify-content-center">
                        <div class="col-md-9">
                            <div class="blog_details_cont">
                                <span class="blog_date">Pasumai Palangal | Thoothukudi | 4 min read</span>
                                <h2 class="blog_title text-capitalize">Strawberries vs. Raspberries: Which Is Better for You?</h2>
                                <div class="blog_author_cont d-flex align-items-center py-3">
                                    <span class="author_name me-5"><font>Posted by</font> Pasumai Palangal</span>
                                    <span class="author_position me-5"><font>In:</font> Imported Fruits</span>
                                    <span class="author_comment"><font>Comments:</font> 0</span>
                                </div>
                                <p class="blog_desc py-3">Stop grabbing the first red carton you see at your fruit shop in Thoothukudi. While most shoppers at Pasumai Palangal in Thoothukudi default to the familiar strawberry, they are often walking right past a nutritional powerhouse that might actually suit their health goals better: the raspberry.</p>

                                <p class="blog_desc py-3">If you're hunting for the best imported fruits shop in Thoothukudi, you need to know what you're paying for. Here is the brutal, honest breakdown of the berry battle.</p>
                                
                                <h3 class="blog_section_title pt-4">The Case for the Strawberry: The Immunity King</h3>
                                <p class="blog_desc py-3">Strawberries are the crowd-pleasers. If you visit a <strong>juice shop in Thoothukudi</strong> or a <strong>cafe fruits spot nearby</strong>, you'll likely find these at the centre of the menu.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>Vitamin C Powerhouse:</strong> One serving packs more Vitamin C than an orange.</li>
                                        <li><i class="fas fa-check"></i> <strong>Skin & Heart Health:</strong> Loaded with folate and potassium.</li>
                                        <li><i class="fas fa-check"></i> <strong>The "Starter" Fruit:</strong> Perfect for children or those new to shopping at a <strong>premium fruits shop in Thoothukudi</strong>.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">The Case for the Raspberry: The Digestive Specialist</h3>
                                <p class="blog_desc py-3">Raspberries are the "intellectual's berry." They are tarter, more delicate, and significantly more functional for specific health issues.</p>
                                <div class="text_style_cont ms-4">
                                    <ul class="list-unstyled style_item">
                                        <li><i class="fas fa-check"></i> <strong>Fibre Overload:</strong> Raspberries have nearly three times the fibre of strawberries. If you are managing digestion or weight, this is your winner.</li>
                                        <li><i class="fas fa-check"></i> <strong>Blood Sugar Control:</strong> With lower sugar and a lower glycemic index, raspberries are the elite choice for diabetic-friendly diets found at our kiwi fruits shop in Thoothukudi.</li>
                                        <li><i class="fas fa-check"></i> <strong>Anti-Inflammatory:</strong> They contain specific polyphenols that help manage chronic inflammation.</li>
                                    </ul>
                                </div>

                                <h3 class="blog_section_title pt-4">Side-by-Side: The Brutal Comparison</h3>
                                <div class="table-responsive pt-3">
                                    <table class="table table-bordered">
                                        <thead class="bg-light">
                                            <tr>
                                                <th>Feature</th>
                                                <th>Strawberry</th>
                                                <th>Raspberry</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><strong>Primary Benefit</strong></td>
                                                <td>Immune Support & Vitamin C</td>
                                                <td>Digestion & Blood Sugar</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Fiber Content</strong></td>
                                                <td>2g</td>
                                                <td>6.5g</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Sugar Content</strong></td>
                                                <td>Moderate</td>
                                                <td>Low</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Best For</strong></td>
                                                <td>Kids, Smoothies, Skin</td>
                                                <td>Diabetics, Weight Loss, Gut Health</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>

                                <h3 class="blog_section_title pt-4">Beyond the Bowl: Gifting and Business</h3>
                                <p class="blog_desc py-3">Health isn't just personal; it's professional. A box of sweets is a lazy gesture. A curated hamper from a fruit gift shop in Thoothukudi is a statement.</p>
                                <p class="blog_desc py-3">For businesses, a corporate gift in Thoothukudi featuring imported berries shows you value the recipient's longevity and health. At Pasumai Palangal, we don't just serve retail customers; our wholesale fruits in the Thoothukudi division ensure that local businesses and gyms have access to the freshest berries and kiwi fruits at scale.</p>

                                <h3 class="blog_section_title pt-4">Final Thoughts</h3>
                                <p class="blog_desc py-3">The logic is simple: Strawberries give you the "shield" (immunity), and raspberries give you the "engine" (digestion). The smartest shoppers at any nearby fruit shop in Thoothukudi know that a mix is the only way to cover all your nutritional bases. Stop settling for one-dimensional nutrition.</p>
                                <p class="blog_desc py-3">Ready to upgrade your fruit game? Visit Pasumai Palangal, the leading premium fruits shop in Thoothukudi, and grab a fresh batch of imported berries today.</p>

                            </div>
                        </div>
                    </div>
                </div>"""

# Replace content between <section class="blog_details...> and <hr>
html = re.sub(r'(<section class="blog_details[^>]*>).*?(<hr>)', r'\1\n' + NEW_BLOG_CONTENT + r'\n                    \2', html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
