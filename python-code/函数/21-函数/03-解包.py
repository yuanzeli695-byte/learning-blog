# 我让列表按位置、字典按名字匹配参数。
def show_three(x, y, z):
    print(x, y, z)

show_three(*[1, 2, 3])
show_three(**{'x': 1, 'y': 2, 'z': 3})
