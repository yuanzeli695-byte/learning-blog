# 我在函数里给 x 赋值，只改变函数内的局部变量。
x = 10

def show_scope():
    x = 20
    print('函数里：', x)

show_scope()
print('函数外：', x)
