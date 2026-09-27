# 整理注：集合主要用来去重和做关系运算。
s={1,2,3,45,6,2}
print(list(s))

#关系运算
hobbies1={'吃饭','睡觉','看书','钢琴','跳舞','英语'}
hobbies2={'吃饭','睡觉','追剧'}
res = hobbies1 & hobbies2
print(res)

# 取并集

res2=hobbies1 | hobbies2
print(res2)

#取差集

print(hobbies1-hobbies2)

#对称差集
print(hobbies2^hobbies1)

#去重
l=['a','b','c','z','k']
print(set(l))

s={1,2,3,4}
s.update([4,5,6])
print(s)
s2={3,4,5}
s3=s.intersection(s2)
print(s3)

s3={9}
s.remove(5)
s.discard(5)
s.add(6)
res3=s.isdisjoint(s3)
print(res3)
