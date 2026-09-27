# 我先更新计数器，再决定跳过或退出。
num = 0
while num < 6:
    num += 1
    if num == 2:
        continue
    if num == 4:
        break
    print(num)
