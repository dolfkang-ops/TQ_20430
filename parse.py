import re
import html
from html.parser import HTMLParser

with open('page.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

# Let's extract text cleanly
class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.imgs = []
    def handle_data(self, data):
        t = data.strip()
        if t:
            self.text.append(t)
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attr_dict = dict(attrs)
            if 'src' in attr_dict:
                self.imgs.append(attr_dict['src'])

parser = HTMLTextExtractor()
parser.feed(raw_html)

with open('extracted_text.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(parser.text))

with open('extracted_imgs.txt', 'w', encoding='utf-8') as out:
    for img in sorted(set(parser.imgs)):
        out.write(img + '\n')

print(f"Extracted {len(parser.text)} text lines, {len(set(parser.imgs))} unique images.")
