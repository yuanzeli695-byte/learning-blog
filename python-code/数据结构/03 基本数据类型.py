# 整理注：字典用键取值，嵌套列表和字典可逐层索引。
 # dic = {'name':'张大仙',
# #        'age':73,
# #        'height':150,
# #        'salary':180
# #        }
# #
# # print(dic['name'])
# # print(dic['salary'])
# #
# # person = [
# #        {'name':'张大仙','age':20,'salary':100,'hobbies':['可乐','厕所','烫头']},
# #        {'name':'hanxin','age':23,'salary':100,'hobbies':['可乐','厕所','烫头']},
# #        {'name':'libai','age':30,'salary':100,'hobbies':['可乐','厕所','烫头']}
# #
# # ]
# #
# # print(person[0])
# # print(person[1])
# # print(person[2])
# #
# # print(person[2]['hobbies'][2])
# #
#
#
#
# #bool类
#
# # a=True
# # b=False
# # print(type(a))
# # print(type(b))
# #
# # a=1
# # b=2
# # c=None
# #
# # name = 'zhangdaxian'
# # l = ['a','b','name']
# #
# # print(id(name))
# # print(id(l[2]))
# #
# # name='zhangdaxian1'
# # l=['a','b',name]
# # name='libai'
# # print(l[2])
#
#
#
#
#
# l1=['a','b',]
# l2=['x','y',]
# l1.append(l2)
# print(id(l1),id(l2))
# l2.append(l1)
# print(id(l1),id(l2))
#
#
# # 不管直接引用或者间接引用,只要引用计数为零则直接被回收机制回收
from tokenize import group
