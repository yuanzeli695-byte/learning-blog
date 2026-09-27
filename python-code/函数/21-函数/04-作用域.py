# 函数内赋值产生局部绑定，外部的 x 保持原值。
x = 10

def show_scope():
    x = 20
    print('函数里：', x)

show_scope()
print('函数外：', x)
