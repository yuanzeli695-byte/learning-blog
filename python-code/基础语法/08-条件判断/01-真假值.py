# bool 可以查看一个值在条件判断中的真假。
for value in (0, None, '', [], {}, 1, 'hello'):
    print(repr(value), bool(value))
