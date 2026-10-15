"""Достает JSON из <script id="state"> артефакта и пишет в файл.
Использование: python3 tools/extract_state.py <artifact.html> <out.json>"""
import json, re, sys

html = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r'<script type="application/json" id="state">(.*?)</script>', html, re.S)
if not m:
    sys.exit("state не найден")
data = json.loads(m.group(1))
with open(sys.argv[2], "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ok →", sys.argv[2])
