import json

with open('review_info.json', 'rb') as f:
    raw = f.read()

data = json.loads(raw.decode('utf-8'))
for item in data.get('data', {}).get('likedList', []):
    print(f"{item.get('code')}: count={item.get('count')}")
