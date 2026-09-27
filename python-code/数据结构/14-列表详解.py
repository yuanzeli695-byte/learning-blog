# 整理注：比较 append 与 extend 时，观察列表长度和元素变化。
msg=['张大仙',84,1.88,False]
print(type(msg))


print(list('hello'))
print(list({'李白', '武则天', '孙尚香'}))




#内置方法
l=['李兴云','姬如雪','园田']

#按索引取值
print(l[1],l[-1])
l.append(5)
print(l)

#插入
l.insert(2,'李淳风')
l2=['梵音天','秒成天','玄净天']
for i in l2:
    l.append(i)
print(l)

#extend
l.extend(l2)
print(l)
