# 每个 yield 产出一个值，并保留当前执行位置。
def numbers():
    print("开始生成")
    yield 1
    yield 2
    yield 3


generator = numbers()
print("已经创建，尚未执行函数体")
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator, "结束"))  # 耗尽时返回这里指定的默认值
