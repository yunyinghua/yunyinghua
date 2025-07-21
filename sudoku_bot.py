import os
import re

title = os.environ.get("ISSUE_TITLE", "")
print(f"Issue title: {title}")

# 校验格式
if not title.startswith("sudoku|set|"):
    print("不是合法格式")
    exit(0)

try:
    _, _, row_s, col_s, value_s = title.strip().split("|")
    row = int(row_s[1:])  # r1 → 1
    col = int(col_s[1:])  # c3 → 3
    value = int(value_s)
except Exception as e:
    print("解析失败:", e)
    exit(1)

print(f"设置格子：第 {row} 行，第 {col} 列，值为：{value}")

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到目标行（README 中表格有标题和分割线，从第3行开始才是棋盘）
target_line_index = row + 1  # 行索引从 0 开始，第1行是表头，第2行是 --- 分隔线
if target_line_index >= len(lines):
    print("找不到目标行")
    exit(1)

# 替换目标列
row_line = lines[target_line_index]
cells = row_line.strip().split("|")

# 注意：split 后有空白项，真实内容从 cells[1] 开始
if col >= len(cells) - 1:
    print("找不到目标列")
    exit(1)

old_cell = cells[col].strip()
print(f"🔍 原始内容：{old_cell}")

if not old_cell.startswith("["):  # 如果是已有数字，就跳过或提示
    print("这个格子已被填写，跳过")
    exit(0)

cells[col] = f" {value} "

# 拼接回去
lines[target_line_index] = "|".join(cells) + "\n"

with open(readme_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("README.md 已更新")
