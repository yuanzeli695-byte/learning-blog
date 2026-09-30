# 列表交给下一层调用处理，普通元素直接打印。
def show_values(items):
    for item in items:
        if isinstance(item, list):
            show_values(item)
        else:
            print(item, end=" ")


show_values([1, 2, [3, 4, [5]]])
print()  # 换行，输出依次为 1 2 3 4 5
