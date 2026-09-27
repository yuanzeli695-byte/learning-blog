# 我用 nonlocal 修改上一层函数里的 x，不让内部函数递归调用自己。
def outer():
    x = 20

    def inner():
        nonlocal x
        x = 30

    inner()
    print('外层局部变量：', x)

outer()
