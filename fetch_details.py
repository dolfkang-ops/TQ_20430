import urllib.request
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://m.thankqcamping.com/resv/view.hbb?cseq=20430'
}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

# 1. 배치도 정보
map_html = fetch('https://m.thankqcamping.com/resv/pop_mapimg.hbb?cseq=20430')
with open('map_info.html', 'w', encoding='utf-8') as f:
    f.write(map_html)

# 2. 사진 갤러리 정보
pic_html = fetch('https://m.thankqcamping.com/resv/pop_picview.hbb?cseq=20430&site_tp=')
with open('pic_info.html', 'w', encoding='utf-8') as f:
    f.write(pic_html)

# 3. 사이트 목록 ajax 호출 시도 (POST or GET)
try:
    # axResCampSite.hbb parameters
    # Let's inspect decoded_utf-8.html for axResCampSite
    print("Fetched map and pic HTMLs.")
except Exception as e:
    print(e)
