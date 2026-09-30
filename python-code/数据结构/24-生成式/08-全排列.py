# 四个不重复字符会输出 24 种排列；到末层输出后直接返回。
def permutation(items, level):
    if level == len(items):
        print("".join(items))
        return

    for index in range(level, len(items)):
        items[level], items[index] = items[index], items[level]
        permutation(items, level + 1)
        items[level], items[index] = items[index], items[level]  # 回溯：恢复现场


letters = list("abcd")
permutation(letters, 0)
print("排列结束后的原列表：", letters)  # ['a', 'b', 'c', 'd']
