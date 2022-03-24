#! /home/kiwi/.pyenv/shims/python3

pt = "list.txt"
rows: list = []
with open(pt, 'r') as fp:
    for i in fp:
        if not i == "\n":
            rows.append(i)

rows = list(set(rows))
rows.sort()

with open("result.txt", "w", encoding="utf-8") as fp:
    fp.writelines(rows)
