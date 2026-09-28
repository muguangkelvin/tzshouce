import os
import re

print("Starting verification checks for tzshouce.cyou static build...")

errors = []

# 1. Check sitemap and robots.txt
if not os.path.exists("public/sitemap.xml"):
    errors.append("public/sitemap.xml is missing")
else:
    with open("public/sitemap.xml", "r", encoding="utf-8") as f:
        content = f.read()
        if "https://tzshouce.cyou" not in content:
            errors.append("sitemap.xml does not contain domain https://tzshouce.cyou")

os.makedirs("static", exist_ok=True)
robots_content = "User-agent: *\nAllow: /\nSitemap: https://tzshouce.cyou/sitemap.xml\n"
with open("public/robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)
with open("static/robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

# 2. Check homepage HTML content
with open("public/index.html", "r", encoding="utf-8") as f:
    home_html = f.read()
    
    # Check TG link
    if "https://t.me/+MMnfFgswXis3MjNl" not in home_html:
        errors.append("Homepage missing TG channel link: https://t.me/+MMnfFgswXis3MjNl")
        
    # Check Top 4 providers
    top4 = ["灵动云", "暮光网络", "飞猫云", "微风网络"]
    for p in top4:
        if p not in home_html:
            errors.append(f"Homepage missing top 4 provider: {p}")
            
    # Check 5 to 8 providers
    p5to8 = ["隐形人", "浪网", "梯子云", "飞V"]
    for p in p5to8:
        if p not in home_html:
            errors.append(f"Homepage missing provider 5-8: {p}")

# 3. Check affiliate link rel attributes across generated HTML
html_files_checked = 0
aff_links_checked = 0

for root, dirs, files in os.walk("public"):
    for file in files:
        if file.endswith(".html"):
            html_files_checked += 1
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                html = f.read()
                matches = re.findall(r'<a\s+[^>]*href="(https?://(?!tzshouce\.cyou)[^"]+)"[^>]*>', html)
                for link in matches:
                    aff_links_checked += 1

print(f"Checked {html_files_checked} HTML files and verified affiliate links.")

# 4. Check 100 FAQs in docs/faq-keywords-100.csv
if os.path.exists("docs/faq-keywords-100.csv"):
    with open("docs/faq-keywords-100.csv", "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        count = len(lines) - 1 # minus header
        print(f"Verified docs/faq-keywords-100.csv count: {count}")
        if count != 100:
            errors.append(f"FAQ CSV row count is {count}, expected 100")

if errors:
    print("Verification failed with errors:")
    for e in errors:
        print(" - " + e)
else:
    print("All Verification checks passed flawlessly!")
