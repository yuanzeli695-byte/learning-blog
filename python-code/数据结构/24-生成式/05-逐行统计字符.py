# StringIO 模拟文本文件；长度包含每行末尾的换行符。
from io import StringIO


with StringIO("第一行\n第二行\n") as file:
    total = sum(len(line) for line in file)

print(total)  # 8：每行 3 个汉字和 1 个换行符
