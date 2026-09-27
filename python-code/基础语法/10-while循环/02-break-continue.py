# 先更新计数器，再决定 continue 或 break。
num = 0
while num < 6:
    num += 1
    if num == 2:
        continue
    if num == 4:
        break
    print(num)
