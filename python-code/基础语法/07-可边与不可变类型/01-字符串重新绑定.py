# name 的新值不是对原字符串的原地修改。
name = 'zhangdaxian'
before = id(name)
name = 'libai'
print(before, id(name), name)
