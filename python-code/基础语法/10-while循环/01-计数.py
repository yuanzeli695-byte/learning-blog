# 每轮末尾更新计数器，否则可能一直循环。
num = 0
while num < 5:
    print(num)
    num += 1
print('循环结束了')
