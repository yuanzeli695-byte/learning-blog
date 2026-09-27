# nonlocal 指向上一层函数里的局部变量。
def outer():
    x = 20

    def inner():
        nonlocal x
        x = 30

    inner()
    print('外层局部变量：', x)

outer()
