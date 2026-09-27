# 我重新赋值时，name 指向了另一个字符串。
name = 'zhangdaxian'
before = id(name)
name = 'libai'
print(before, id(name), name)
