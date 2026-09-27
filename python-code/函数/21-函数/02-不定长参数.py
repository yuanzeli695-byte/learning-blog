# *args 是元组，**kwargs 是字典。
def show_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

show_arguments(1, 2, 3, name='张大仙', age=18)
