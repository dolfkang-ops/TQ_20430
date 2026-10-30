import urllib.request
import json

req = urllib.request.Request(
    'https://m.thankqcamping.com/talk/api/ax_camp_review_info.hbb',
    data=b'campSeq=20430',
    headers={'User-Agent': 'Mozilla/5.0'}
)
resp = urllib.request.urlopen(req)
raw = resp.read()

# Let's test decoding
for enc in ['utf-8', 'euc-kr', 'cp949']:
    try:
        data = json.loads(raw.decode(enc))
        print(f"=== {enc} SUCCESS ===")
        print("CampName:", data['data']['campName'])
        for item in data['data']['likedList'][:12]:
            print(f"  - {item['value']}: {item['count']}명")
        break
    except Exception as e:
        print(f"{enc} failed: {e}")
