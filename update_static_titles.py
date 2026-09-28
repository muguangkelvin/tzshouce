import os
import glob
import re

static_files = [
    "content/about.md",
    "content/affiliate-disclosure.md",
    "content/contact.md",
    "content/corrections.md",
    "content/disclaimer.md",
    "content/editorial-policy.md",
    "content/methodology.md",
    "content/privacy.md",
    "content/terms.md"
]

clean_titles = {
    "content/about.md": "关于我们与团队介绍",
    "content/affiliate-disclosure.md": "透明化联盟合作与推广政策说明",
    "content/contact.md": "联系我们与问题反馈渠道",
    "content/corrections.md": "内容纠错与更新维护政策",
    "content/disclaimer.md": "免责声明与官方防走丢入口说明",
    "content/editorial-policy.md": "独立客观评测与编辑原则规范",
    "content/methodology.md": "梯子与机场评测标准与测试方法论",
    "content/privacy.md": "隐私政策与数据保护声明",
    "content/terms.md": "服务条款与用户协议"
}

for path, title in clean_titles.items():
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r'title:\s*["\']?.*?["\']?\n', f'title: "{title}"\n', text, count=1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

print("Static page titles updated cleanly!")
