# 我直接修改列表的元素，而不是重新创建列表。
names = ['zhangdaxian', 'libai']
before = id(names)
names[1] = 'luna'
print(names, before == id(names))
