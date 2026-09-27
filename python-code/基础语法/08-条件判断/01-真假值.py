# 我把常见的空值逐个转成布尔值。
for value in (0, None, '', [], {}, 1, 'hello'):
    print(repr(value), bool(value))
