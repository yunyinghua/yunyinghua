import os

title = os.environ.get("ISSUE_TITLE", "")
print(f"Issue title: {title}")

if not title.startswith("sudoku|set|"):
    print("❌ 不是一个合法的数独操作 issue")
    exit(0)

_, _, row_s, col_s, value_s = title.strip().split("|")

row = int(row_s[1:])
col = int(col_s[1:])
value = int(value_s)

print(f"📍 需要设置格子：第 {row} 行，第 {col} 列，值为：{value}")
