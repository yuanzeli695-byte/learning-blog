# 我从靠近函数的装饰器开始包，调用时却先进入最外层。
def first(func):
    def wrapper(*args, **kwargs):
        print('开始 first')
        result = func(*args, **kwargs)
        print('结束 first')
        return result
    return wrapper

def second(func):
    def wrapper(*args, **kwargs):
        print('开始 second')
        result = func(*args, **kwargs)
        print('结束 second')
        return result
    return wrapper

@second
@first
def home(value):
    print('函数本身：', value)

home(1)
