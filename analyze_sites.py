import re
import json

with open('decoded_utf-8.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find notices
notices = re.findall(r'<li[^>]*class=[\'"][^\'"]*notice[^\'"]*[\'"][^>]*>([\s\S]*?)</li>', html, re.I)
print(f"Found {len(notices)} notices:")
for n in notices:
    clean_n = re.sub(r'<[^>]+>', ' ', n).strip()
    clean_n = ' '.join(clean_n.split())
    print("-", clean_n[:120])

# look for site list or zone list
# check if there are divs or elements for sites
site_elements = re.findall(r'<div[^>]*class=[\'"][^\'"]*site[^\'"]*[\'"][^>]*>([\s\S]*?)</div>', html, re.I)
print(f"Site elements count: {len(site_elements)}")

# Find all image links and see their context
img_tags = re.findall(r'<img[^>]+>', html, re.I)
print(f"Total img tags: {len(img_tags)}")
with open('all_imgs_info.txt', 'w', encoding='utf-8') as out:
    for tag in img_tags:
        out.write(tag + '\n')

# Check links or ajax urls
ajax_calls = re.findall(r'(\/resv\/[a-zA-Z0-9_\.]+\.hbb[^\'\"\s]*)', html)
print("Resv endpoints:", set(ajax_calls))
