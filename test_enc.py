import json

with open('review_info.json', 'r', encoding='utf-8') as f:
    text = f.read()

# print unicode escape
print(text[:500])
