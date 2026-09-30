# 字典迭代得到键，不需要用数字下标访问。
scores = {"语文": 88, "数学": 92, "英语": 90}
iterator = iter(scores)

print(next(iterator))  # 语文
print(next(iterator))  # 数学
print(next(iterator))  # 英语
