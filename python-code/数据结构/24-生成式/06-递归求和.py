# 这里的练习范围是非负整数，到 0 就不再调用自己。
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


print(recursive_sum(5))  # 15
print(recursive_sum(0))  # 0
