import urllib.request
import re

url = 'https://m.thankqcamping.com/resv/list.hbb?cseq=20430'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        with open('list_page.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Fetched list_page.html", len(html))
        # Search for site names and prices
        clean = re.sub(r'<[^>]+>', '\n', html)
        for line in clean.splitlines():
            line = line.strip()
            if any(k in line for k in ['사이트', 'zone', '원', 'A-', 'B-', 'C-', 'D-', 'E-', 'F-', 'G-', 'H-', 'P-']):
                print("Line:", line[:100])
except Exception as e:
    print("Error:", e)
