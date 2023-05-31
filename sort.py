pt: str = "list.txt"
enc: str = "utf-8"
rows: list = []
with open(pt, 'r', encoding=enc) as fp:
    for i in fp:
        if not i == "\n":
            rows.append(i)

# 重複の除外
rows = list(set(rows))
rows.sort()

with open(pt, "w", encoding=enc) as fp:
    fp.writelines(rows)
