content = open('index.html', encoding='utf-8').read()

# Add align-items-stretch to the row
content = content.replace(
    '               <div class="prdc_ctg_wrap mx-2">\n                  <div class="row">',
    '               <div class="prdc_ctg_wrap mx-2">\n                  <div class="row align-items-stretch">'
)

# Add h-100 to both columns so they stretch equally
content = content.replace(
    '                     <div class="col-xl-4 px-md-0">',
    '                     <div class="col-xl-4 px-md-0 d-flex flex-column">'
)
content = content.replace(
    '                        <div class="prdc_ctg_content_wrap">',
    '                        <div class="prdc_ctg_content_wrap h-100">',
    1  # only first occurrence (inside produce_category_section)
)
content = content.replace(
    '                     <div class="col-xl-8 px-0">',
    '                     <div class="col-xl-8 px-0 d-flex flex-column">',
    1
)
content = content.replace(
    '                        <div class="tab-content" id="pills-tabContent">',
    '                        <div class="tab-content h-100" id="pills-tabContent">',
    1
)

open('index.html', 'w', encoding='utf-8').write(content)
print("Done")
