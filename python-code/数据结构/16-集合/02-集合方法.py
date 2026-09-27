# 转为集合可以去重，但不能依赖元素顺序。
print(set(['a', 'a', 'b']))
values = {1, 2, 3, 4}
values.update([4, 5, 6])
print(values.intersection({3, 4, 5}))
values.remove(5)
values.discard(5)  # 不存在也不会报错
print(values.isdisjoint({9}))
