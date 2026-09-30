# 同一个列表可以创建新迭代器；同一个耗尽的迭代器不能重来。
items = ["a", "b", "c"]
iterator = iter(items)

for item in iterator:
    print(item)

print(list(iterator))  # []：原迭代器已经耗尽
print(list(iter(items)))  # ['a', 'b', 'c']：重新创建后可以再取
