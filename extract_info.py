import re
from html.parser import HTMLParser

with open('decoded_utf-8.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find images
imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html_content, re.IGNORECASE)
camp_imgs = [img for img in set(imgs) if any(x in img for x in ['thankq', 'upload', 'camp', 'thumb', 'file', 'jpg', 'png', 'jpeg']) and 'common' not in img and 'icon' not in img and 'btn' not in img and 'logo' not in img and 'banner' not in img]

print("=== FOUND CAMP IMAGES ===")
for img in camp_imgs[:25]:
    print(img)

# Strip script and style tags
text_clean = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
text_clean = re.sub(r'<style.*?</style>', '', text_clean, flags=re.DOTALL | re.IGNORECASE)
text_clean = re.sub(r'<[^>]+>', '\n', text_clean)
lines = [l.strip() for l in text_clean.splitlines() if l.strip()]

with open('clean_text.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"\nWrote {len(lines)} cleaned lines.")
