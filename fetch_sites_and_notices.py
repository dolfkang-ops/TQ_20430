import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://m.thankqcamping.com/resv/view.hbb?cseq=20430',
    'X-Requested-With': 'XMLHttpRequest'
}

# 1. Fetch notices
noti_ids = [8887, 8886, 8836, 8828, 8750, 8713, 8669, 8650]
notices_data = []

for nid in noti_ids:
    url = f'https://m.thankqcamping.com/resv/pop_notiview.hbb?cseq=20430&brd_id={nid}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            # extract title and text
            clean = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
            clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
            clean = re.sub(r'<[^>]+>', '\n', clean)
            lines = [l.strip() for l in clean.splitlines() if l.strip()]
            notices_data.append({'id': nid, 'text': '\n'.join(lines)})
    except Exception as e:
        print(f"Error fetching notice {nid}: {e}")

with open('notices_all.txt', 'w', encoding='utf-8') as f:
    for n in notices_data:
        f.write(f"\n================ NOTICE {n['id']} ================\n")
        f.write(n['text'])

print(f"Fetched {len(notices_data)} notices.")

# 2. Try fetching axResCampSite.hbb
post_data = urllib.parse.urlencode({
    'cseq': '20430',
    'res_dt': '20261107',
    'res_edt': '20261108',
    'site_tp': ''
}).encode('utf-8')

req = urllib.request.Request('https://m.thankqcamping.com/resv/axResCampSite.hbb', data=post_data, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        site_res = resp.read().decode('utf-8', errors='ignore')
        with open('sites_res.html', 'w', encoding='utf-8') as f:
            f.write(site_res)
        print("Fetched axResCampSite, size:", len(site_res))
except Exception as e:
    print(f"Error fetching axResCampSite: {e}")
