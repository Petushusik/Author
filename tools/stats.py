"""Статистика черновика: знаки, слова, абзацы, длина каждого абзаца.
Pages пишет Shift+Enter как U+2028, поэтому считаются и абзацы (Enter), и строки (Enter + Shift+Enter).
Использование: python3 tools/stats.py <draft.txt> [--full]"""
import sys

text = open(sys.argv[1], encoding="utf-8").read()
paras = [p for p in text.split("\n") if p.strip()]
lines = [p for p in text.replace(" ", "\n").split("\n") if p.strip()]
lens = [len(p) for p in lines]
fmt = lambda n: f"{n:,}".replace(",", " ")
print(f"Знаков: {fmt(len(text))} | без пробелов: {fmt(sum(1 for c in text if not c.isspace()))}")
print(f"Слов: {fmt(len(text.split()))} | абзацев (Enter): {len(paras)} | строк (с Shift+Enter): {len(lines)}")
print(f"Строка: средняя {sum(lens)//len(lens)}, мин {min(lens)}, макс {max(lens)}")
if "--full" in sys.argv:
    for i, n in enumerate(lens, 1):
        print(f"{i:>5}  {n:>6}  {lines[i-1][:60]}")
