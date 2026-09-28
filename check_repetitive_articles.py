import os
import re

content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"

repetitive_titles = []
repetitive_bodies = []

for root, dirs, files in os.walk(content_dir):
    for f_name in files:
        if not f_name.endswith(".md"):
            continue
        f_path = os.path.join(root, f_name)
        with open(f_path, "r", encoding="utf-8") as f:
            text = f.read()

        m_title = re.search(r'title:\s*"(.*?)"', text)
        if m_title:
            title_val = m_title.group(1)
            if "\u7b2c" in title_val and "\u671f" in title_val:
                repetitive_titles.append((f_path, title_val))

        if "\u9762\u5411\u7ed3\u7247" in text or "\u4e3a\u4ec0\u4e48\u9009\u62e9\u9ad8\u8d28\u97cf" in text or "面向翻墙与科学上网新手" in text or "为什么选择高质量梯子机场？" in text:
            repetitive_bodies.append(f_path)

print(f"Found {len(repetitive_titles)} files with repetitive titles.")
print(f"Found {len(repetitive_bodies)} files with repetitive body text.")

for p, t in repetitive_titles:
    rel = os.path.relpath(p, content_dir)
    print("Repetitive Title:", rel)

for p in repetitive_bodies:
    rel = os.path.relpath(p, content_dir)
    print("Repetitive Body:", rel)
