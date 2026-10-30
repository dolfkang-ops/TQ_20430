import re

with open('decoded_utf-8.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for site names, zone names, and prices
matches = re.findall(r'([A-Za-z0-9가-힣\s\-]+사이트[\s\S]{1,100}?[0-9,]+원)', html)
for m in matches[:10]:
    print("Match:", m.strip())

# Check for any JSON object inside html
json_blocks = re.findall(r'(\{[\s\S]*?\})', html)
site_info_blocks = []
for b in json_blocks:
    if any(k in b for k in ['site_name', 'site_nm', 'price', 'amt', 'rate', 'zone_nm']):
        site_info_blocks.append(b[:200])

print(f"JSON blocks with site keywords: {len(site_info_blocks)}")
for b in site_info_blocks[:5]:
    print("-", b)
