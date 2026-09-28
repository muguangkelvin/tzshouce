import os
import glob
import re

files = glob.glob('content/**/*.md', recursive=True)

with open('all_titles.txt', 'w', encoding='utf-8') as out:
    for f in sorted(files):
        with open(f, 'r', encoding='utf-8') as fp:
            text = fp.read()
            m = re.search(r'title:\s*["\']?(.*?)["\']?\n', text)
            title = m.group(1).strip() if m else "NO TITLE"
            out.write(f"{f} | {title}\n")

print(f"Written titles for {len(files)} files to all_titles.txt")
