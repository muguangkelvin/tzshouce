import glob
import os
import re

files = glob.glob('content/**/*.md', recursive=True)
print(f"Total markdown files: {len(files)}")

titles = {}
duplicates = []
template_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        text = fp.read()
        m = re.search(r'title:\s*["\']?(.*?)["\']?\n', text)
        if m:
            t = m.group(1).strip()
            if t in titles:
                duplicates.append((t, f, titles[t]))
            else:
                titles[t] = f
        if '面向翻墙与科学上网新手' in text or '第5期' in text or '第4期' in text or '模板' in text:
            template_files.append(f)

print(f"Duplicate titles count: {len(duplicates)}")
for d in duplicates[:10]:
    print(f"Duplicate: {d[0]} in {d[1]} and {d[2]}")

print(f"Template/Repetitive phrase occurrences: {len(template_files)}")
for tf in template_files[:10]:
    print(f"Template in: {tf}")
