# 字典形式用占位符的名字对应具体值。
info = '我叫%s，来自%s' % ('张大仙', '广东')
print(info)
named = '我叫%(name)s，来自%(city)s' % {'name': '张大仙', 'city': '广东'}
print(named)
