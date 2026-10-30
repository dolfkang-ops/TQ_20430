import json

with open('review_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

reviews = data.get('data', {}).get('content', [])
print(f"Total reviews in page 0: {len(reviews)}")

for i, r in enumerate(reviews[:10]):
    user = r.get('nickName') or r.get('userId') or '캠퍼'
    score = r.get('score', 5)
    site = r.get('siteName') or r.get('roomName') or ''
    date = r.get('regDt') or r.get('resDate') or ''
    content = r.get('content') or r.get('reviewText') or ''
    liked = r.get('likedTextList') or []
    print(f"\n[{i+1}] {user} ({site}) - 평점: {score} / {date}")
    print(f"내용: {content.strip()}")
    if liked:
        print(f"키워드: {liked}")
