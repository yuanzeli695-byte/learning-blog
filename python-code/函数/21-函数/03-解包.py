# * 按位置解包，** 按键名解包。
def show_three(x, y, z):
    print(x, y, z)

show_three(*[1, 2, 3])
show_three(**{'x': 1, 'y': 2, 'z': 3})
