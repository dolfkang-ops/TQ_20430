import json

with open('review_list.json', 'rb') as f:
    raw = f.read()

# Try loading as json
data = json.loads(raw.decode('utf-8'))

with open('reviews_clean.txt', 'w', encoding='utf-8') as out:
    for i, r in enumerate(data.get('data', {}).get('content', [])):
        out.write(f"--- REVIEW {i+1} ---\n")
        out.write(f"Nick: {r.get('nickName')} | Score: {r.get('score')} | Site: {r.get('siteName')} | Date: {r.get('regDt')}\n")
        out.write(f"Content: {r.get('content')}\n")
        out.write(f"Keywords: {r.get('likedTextList')}\n\n")

print("Saved reviews_clean.txt")
