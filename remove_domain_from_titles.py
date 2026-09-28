import os
import re

# 1. Update hugo.toml
hugo_path = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\hugo.toml"
if os.path.exists(hugo_path):
    with open(hugo_path, "r", encoding="utf-8") as f:
        hugo_content = f.read()
    hugo_content = hugo_content.replace("(tzshouce.cyou)", "").replace(" tzshouce.cyou", "")
    with open(hugo_path, "w", encoding="utf-8") as f:
        f.write(hugo_content)
    print("Updated hugo.toml!")

# 2. Update all .md files in content/
content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"

count = 0
for root, dirs, files in os.walk(content_dir):
    for f_name in files:
        if not f_name.endswith(".md"):
            continue
        file_path = os.path.join(root, f_name)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        new_text = text
        # Remove tzshouce.cyou from title front matter and # H1 headings
        # e.g., title: "关于我们 - 梯子手册 tzshouce.cyou" -> title: "关于我们 - 梯子手册"
        # # 关于我们 - 梯子手册 tzshouce.cyou -> # 关于我们 - 梯子手册
        new_text = re.sub(r'(title:\s*".*?)(\s+tzshouce\.cyou|\s*\(tzshouce\.cyou\))(")', r'\1\3', new_text)
        new_text = re.sub(r'(#\s+.*?)(\s+tzshouce\.cyou|\s*\(tzshouce\.cyou\))(\n|$)', r'\1\3', new_text)
        new_text = new_text.replace(" 梯子手册 tzshouce.cyou ", " 梯子手册 ")
        new_text = new_text.replace("梯子手册 tzshouce.cyou", "梯子手册")

        if new_text != text:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_text)
            count += 1

print(f"Updated {count} content markdown files to remove tzshouce.cyou from titles and headings!")

# 3. Update layout templates if any contain tzshouce.cyou in title headings
layouts_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\layouts"
l_count = 0
for root, dirs, files in os.walk(layouts_dir):
    for f_name in files:
        if not f_name.endswith(".html"):
            continue
        file_path = os.path.join(root, f_name)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        new_text = text.replace(" tzshouce.cyou", "").replace("(tzshouce.cyou)", "")
        if new_text != text:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_text)
            l_count += 1

print(f"Updated {l_count} layout HTML files!")
