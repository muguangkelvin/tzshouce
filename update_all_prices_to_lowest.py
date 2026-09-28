import os
import re

price_map = {
    "灵动云": "¥15/月起",
    "暮光网络": "¥20/月起",
    "飞猫云": "折合 ¥7/月",
    "微风网络": "¥12/月起",
    "隐形人": "¥18/月起",
    "浪网 WaveNet": "¥25/月起",
    "浪网": "¥25/月起",
    "梯子云 LadderCloud": "¥15/月起",
    "梯子云": "¥15/月起",
    "飞V": "¥16/月起",
    "全球云": "¥20/月起",
    "星岛梦": "¥15/月起",
    "光速云": "¥18/月起",
    "唯兔云": "¥16/月起",
    "U1S1": "¥12/月起",
    "极连云": "¥15/月起",
    "光年梯": "¥18/月起",
    "Sogo云": "¥15/月起",
    "宇宙云": "¥22/月起",
    "二猫云": "¥9.9/月起",
    "一翻云": "¥15/月起",
    "边缘节点": "¥18/月起",
    "可信云": "¥20/月起",
    "速界": "¥16/月起",
    "快狸": "¥12/月起",
    "无忧": "¥15/月起",
    "灵猫": "¥14/月起",
    "闪跃": "¥20/月起",
    "飞为": "¥18/月起",
    "跨界": "¥22/月起"
}

# 1. Update layouts/index.html
index_layout = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\layouts\index.html"
if os.path.exists(index_layout):
    with open(index_layout, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace in grid cards & comparison table
    html = html.replace(">官网为准<", ">¥15/月起<")
    html = html.replace(">结算页为准<", ">¥12/月起<")

    for brand, price in price_map.items():
        # Match table row with brand name and 官网为准 / 结算页为准
        pattern = re.compile(rf'(<td>.*?{brand}.*?</td>\s*<td>)(官网为准|结算页为准|官网结算页为准)(</td>)', re.IGNORECASE)
        html = pattern.sub(rf'\g<1>{price}\g<3>', html)

    with open(index_layout, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated layouts/index.html with lowest prices!")

# 2. Update content/providers/*.md
providers_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\providers"
for f_name in os.listdir(providers_dir):
    if not f_name.endswith(".md"):
        continue
    f_path = os.path.join(providers_dir, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        text = f.read()

    brand_found = None
    for brand in price_map:
        if brand in text:
            brand_found = brand
            break

    low_price = price_map.get(brand_found, "¥15/月起")

    new_text = text.replace("官网为准", low_price)
    new_text = new_text.replace("结算页为准", low_price)
    new_text = new_text.replace("官网结算页为准", low_price)

    if new_text != text:
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(new_text)

print("Updated provider review articles in content/providers/ with lowest prices!")

# 3. Update content/jichang-tuijian/*.md
jichang_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian"
for f_name in os.listdir(jichang_dir):
    if not f_name.endswith(".md"):
        continue
    f_path = os.path.join(jichang_dir, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        text = f.read()

    new_text = text
    for brand, price in price_map.items():
        # Replace 官网为准 / 结算页为准 in tables for this brand
        pattern = re.compile(rf'(<td>.*?{brand}.*?</td>\s*<td>)(官网为准|结算页为准|官网结算页为准)(</td>)', re.IGNORECASE)
        new_text = pattern.sub(rf'\g<1>{price}\g<3>', new_text)

    # General replaces for any leftover
    new_text = new_text.replace("官网为准 (用码8折)", "¥15/月起 (用码8折)")
    new_text = new_text.replace("官网结算页为准", "¥15/月起")

    if new_text != text:
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(new_text)

print("Updated ranking articles in content/jichang-tuijian/ with lowest prices!")
