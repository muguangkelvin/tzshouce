import os
import glob
import re
from collections import defaultdict

files = glob.glob('content/**/*.md', recursive=True)

title_patterns = []
body_hashes = defaultdict(list)

for f_path in files:
    with open(f_path, 'r', encoding='utf-8') as f:
        text = f.read()

    m_title = re.search(r'title:\s*["\']?(.*?)["\']?\n', text)
    title = m_title.group(1).strip() if m_title else "No Title"

    # Check title issues (e.g. 第X期 / 第X讲 / 第X期)
    if re.search(r'第\s*\d+\s*[期讲篇]', title):
        title_patterns.append((f_path, title))

    # Remove frontmatter for body check
    parts = text.split('---', 2)
    body = parts[2].strip() if len(parts) >= 3 else text

    # Collect body snippets
    body_clean = re.sub(r'\s+', ' ', body)
    first_200 = body_clean[:200]
    body_hashes[first_200].append(f_path)

out_lines = []
out_lines.append(f"Total markdown files found: {len(files)}")
out_lines.append(f"\n--- Files with '第X期/讲/篇' in Title ({len(title_patterns)}) ---")
for p, t in title_patterns:
    out_lines.append(f"File: {p} | Title: {t}")

repeated_count = 0
out_lines.append(f"\n--- Repeated Body Snippets (Count > 1) ---")
for snippet, flist in body_hashes.items():
    if len(flist) > 1:
        repeated_count += 1
        out_lines.append(f"\nSnippet repeated across {len(flist)} files:")
        out_lines.append(f"  Snippet: {snippet[:100]}...")
        for f in flist:
            out_lines.append(f"    - {f}")

out_lines.append(f"\nTotal repeated body snippet groups: {repeated_count}")

with open("audit_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Audit complete. Results saved to audit_results.txt")
