# 整理注：后半段用 copy.deepcopy 观察嵌套列表的拷贝。


# girl_friend='human'
# gender='female'
# age=18


# print(girl_friend=='human')
# print(gender=='female')
# print(16<age<84)
#
#
# #逻辑运算符:
# #and逻辑与
# # print(girl_friend== 'human' and gender=='female')
#
#
#
# #not 逻辑非
#
# # print(not True)
#
# print(not 16<age<18)
#
# print(not 0,not'',not[],not{})

#or 逻辑或

#优先级
#not>and>or

 #成员运算符
# print('zhangdaxian' in 'zhangdaxian nishigeyaoguaiba')
#
# l=[1,2,3]
# print(4 in l)
#
# dic={'name':'zhangdaxian','age':84}
# print('zhangdaxian'in dic)
# print('name'in dic)
#
# print('zhangdaxian'not in dic)
# print('name'not in dic)


# l1=['zhang','xu',['li','deng']]
# l2=l1
#
# l1[0]='tank'
# #浅拷贝
# l3=l1.copy()
# print(l3)
# print(id(l1),id(l3))
#
# print(id(l1[1]),id(l1[2]),id(l1[0]))
# print(id(l3[1]),id(l3[2]),id(l3[0]))
#
# l3[0]='zhang'
# l3[1]='ke'
# l3[2]='p'
#
# print(id(l3[1]),id(l3[2]),id(l3[0]))

#深拷贝
l1 = ['张大仙', '徐凤年', ['李淳罡', '邓太阿']]
import copy

l3 = copy.deepcopy(l1)
# print(l3)
# print(id(l1))
# print(id(l3))
# print(id(l1[0]), id(l1[1]), id(l1[2]))
# print(id(l3[0]), id(l3[1]), id(l3[2]))
print(id(l1[2][0]), id(l1[2][1]))
print(id(l3[2][0]), id(l3[2][1]))
