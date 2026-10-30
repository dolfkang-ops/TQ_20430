import re

with open('pic_info.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find all img tags with alt or title or caption
imgs = re.findall(r'<img[^>]+>', text)
for img in imgs:
    if 'image.thankqcamping.com' in img:
        print(img)
