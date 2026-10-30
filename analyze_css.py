import re

with open('current_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check bracket balance
open_braces = css.count('{')
close_braces = css.count('}')
print(f"Braces check: {{ = {open_braces}, }} = {close_braces}")

# Check duplicate selectors
selectors = re.findall(r'([^{]+)\{', css)
sel_list = [s.strip() for s in selectors if not s.strip().startswith('@')]
from collections import Counter
counts = Counter(sel_list)
dups = {k: v for k, v in counts.items() if v > 1}
print(f"Duplicate selectors count: {len(dups)}")
for k, v in list(dups.items())[:15]:
    print(f"  {k}: {v} times")
