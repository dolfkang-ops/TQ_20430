import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://m.thankqcamping.com/resv/view.hbb?cseq=20430',
    'X-Requested-With': 'XMLHttpRequest'
}

# Try GET /resv/ax_camp_review_list.hbb?cseq=20430
urls_to_try = [
    'https://m.thankqcamping.com/resv/ax_camp_review_list.hbb?cseq=20430&page=1',
    'https://m.thankqcamping.com/resv/ax_camp_review_info.hbb?cseq=20430'
]

for url in urls_to_try:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            filename = url.split('/')[-1].split('?')[0] + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Success {url}: {len(content)} chars written to {filename}")
    except Exception as e:
        print(f"Failed {url}: {e}")

# Try POST if GET didn't return much
post_data = urllib.parse.urlencode({'cseq': '20430', 'page': '1', 'page_size': '20'}).encode('utf-8')
try:
    req = urllib.request.Request('https://m.thankqcamping.com/resv/ax_camp_review_list.hbb', data=post_data, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        with open('ax_camp_review_list_post.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"POST ax_camp_review_list: {len(content)} chars")
except Exception as e:
    print(f"POST failed: {e}")
