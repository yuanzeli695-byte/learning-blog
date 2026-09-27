# wraps 保留被装饰函数的名字和文档信息。
from functools import wraps
from time import perf_counter

def count_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print('耗时：', perf_counter() - start)
        return result
    return wrapper

@count_time
def add(x, y):
    return x + y

print(add(2, 3))
