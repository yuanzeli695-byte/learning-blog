# 我用 *args 和 **kwargs 接收不固定数量的参数。
def show_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

show_arguments(1, 2, 3, name='张大仙', age=18)
