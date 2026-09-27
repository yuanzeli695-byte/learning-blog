# 内层终点写成 row + 1，才能包含当前行号。
for row in range(1, 10):
    for col in range(1, row + 1):
        print(f'{col}×{row}={col * row}', end='\t')
    print()
