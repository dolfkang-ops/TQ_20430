import urllib.request
import urllib.parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://m.thankqcamping.com/resv/view.hbb?cseq=20430',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

# 1. ax_camp_review_info
info_data = urllib.parse.urlencode({'campSeq': '20430'}).encode('utf-8')
req = urllib.request.Request('https://m.thankqcamping.com/talk/api/ax_camp_review_info.hbb', data=info_data, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Review Info:", json.dumps(res, ensure_ascii=False, indent=2))
        with open('review_info.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error info:", e)

# 2. ax_camp_review_list
list_data = urllib.parse.urlencode({
    'campSeq': '20430',
    'page': '0',
    'size': '20',
    'sort': 'RECOMMEND',
    'photoOnly': 'false'
}).encode('utf-8')
req2 = urllib.request.Request('https://m.thankqcamping.com/talk/api/ax_camp_review_list.hbb', data=list_data, headers=headers)
try:
    with urllib.request.urlopen(req2) as resp:
        res2 = json.loads(resp.read().decode('utf-8'))
        print(f"Review List count: {len(res2.get('data', {}).get('content', []))}")
        with open('review_list.json', 'w', encoding='utf-8') as f:
            json.dump(res2, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error list:", e)
