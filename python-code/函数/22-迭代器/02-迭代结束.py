# StopIteration 表示没有下一项了，不是继续等待新数据。
iterator = iter(["a", "b", "c"])

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)

print("已取完")
