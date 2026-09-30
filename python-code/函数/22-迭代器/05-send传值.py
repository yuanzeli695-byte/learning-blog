# send 的返回值来自下一次 yield；传入的值交给暂停处的 received。
def receiver(label):
    print(f"{label}：开始")
    while True:
        received = yield None
        print(f"{label}：收到 {received}")


generator = receiver("练习")
print(generator.send(None))  # 先执行到第一个 yield，返回 None
print(generator.send(2))  # received 得到 2，再运行到下一次 yield
print(generator.send(3))
generator.close()  # 示例结束，关闭无限生成器
