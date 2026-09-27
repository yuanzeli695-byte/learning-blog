# 我让内层从 1 遍历到当前行号。
for row in range(1, 10):
    for col in range(1, row + 1):
        print(f'{col}×{row}={col * row}', end='\t')
    print()
