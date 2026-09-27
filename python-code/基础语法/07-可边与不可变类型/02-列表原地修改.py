# 修改元素前后，列表的 id 保持相同。
names = ['zhangdaxian', 'libai']
before = id(names)
names[1] = 'luna'
print(names, before == id(names))
