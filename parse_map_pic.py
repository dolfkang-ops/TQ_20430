import re

with open('map_info.html', 'r', encoding='utf-8') as f:
    map_html = f.read()

print("=== MAP HTML ===")
imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', map_html)
print("Map images:", imgs)

with open('pic_info.html', 'r', encoding='utf-8') as f:
    pic_html = f.read()

print("=== PIC HTML ===")
pic_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', pic_html)
print(f"Gallery images ({len(pic_imgs)}):")
for p in pic_imgs[:20]:
    print(p)
