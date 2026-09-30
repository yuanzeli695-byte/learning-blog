# 只选择一个结果，不必把简单分支拆成很多行。
x = 1
y = 2

if x > y:
    result = x
else:
    result = y

short_result = x if x > y else y
print(result)  # 2
print(short_result)  # 2
