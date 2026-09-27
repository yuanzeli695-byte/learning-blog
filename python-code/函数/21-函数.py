# 整理注：保留原有函数实验；逐段运行比一次执行整个文件更适合复盘。
#coding: utf-8
#@Author: yuanlzeli

#代码冗余
#组织结构不清晰、可读性差
#可维护性、可扩展性差


#函数(具备某一功能的工具)
#先定义
#后调用

#函数的使用


#
# def func1():
#     print('这是我的第一个函数')
#
# func1()
# print(func1)

# a=18
# def func1():
#     print('我是func1')
# def func2():
#     print(func1())
#     print('我是func2')
#
# func2()
# func1()

# def func1(x,y):
#     print((x,y))
#
# func1(6,8)
#
# def add(x,y):
#     # x=26
#     # y=10
#     res=x+y
#     # print(res)
#     return res
# print(add(1,1))
#
# def func():
#     name=input('请输入你的姓名>>>')
#     password=input('请输入你的密码')
#     res=f'你的姓名是{name},你的密码是{password}'
#     print(res)

# def func(*x):
#     res=0
#     for i in x:
#         res+=i
#     return res
#
#
# print(func(1, 2, 3, 4, 5))

# def func(x,y, **kwargs):
#     print(x,y,kwargs)
#
# func(1,2,a=1,b=2,c=3)


# def func(x,y,z):
#     print(x,y,z)
# func(*[1,2,3])

# def func(x,y,z):
#     print(x,y,z)
#
# func(*{'x':1,'y':2,'z':3})
# func(*{'x':1,'y':2,'z':3})

#
# def funcs(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# funcs(1,2,3,4,a=1,b=3,c=4)

# #重中之重
# def func1 (x,y,z):
#     print(x,y,z)
# def func2 (*args,**kwargs):#打包为元组,打包为字典
#     func1(*args,**kwargs)#解包元组,解包字典
#
# func2(1,2,3)
#
#
# #名称空间(namespaces)和作用域
# # import this
#
#
# x=10
# def func1 ():
#     print(x)
# def func2():
#     x=20
#     func1()
# func2()
#
# #名称空间的查找顺序是以定义阶段为基准的,和调用的位置没有任何关系
#
#
# def func1():

# x=10
# def func():
#     global x
#     x=20
#
# func()
# print(x)
#
#
# l=[1,2,3]
# def func2():
#     l.append(4)
#
# func2()
# print(l)

x=10
def func1():
    x=20
    def func2():
        nonlocal x
        x=30
        func2()

func1()
print(x)




# 方案1:
import time
from urllib import response


# def inside(group, s):
#     start=time.time()
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#     end=time.time()
#     print(end-start)


# 方案2""
# 问题:没有修改源代码
# 也没有修改调用方式，
# 同时还加上了新的功能，
# 但是有大量重复代码，

# def inside(group, s):
#
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
# start=time.time()
# inside('蓝色',5)
# end=time.time()
# print(end-start)



# 方案3:
# 解决了方案二的代码冗余问题，
# 也没有修改被装饰对象的源代码，
# 同时还为其增加了新的功能
# 但是被装饰对象的调用方式被修改了
# def inside(group, s):
#
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
# def wrapper():
#     start=time.time()
#     inside('蓝色',3)
#     end=time.time()
#     print(end-start)

# 方案4:
# def inside(group, s,z):
#
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
# # 形参前加*和**是打包的意思,实参中*和**是解包的意思
# def wrapper(*args,**kwargs):
#     start=time.time()
#     inside(*args,**kwargs)
#     end=time.time()
#     print(end-start)
# wrapper('蓝色',3,'跑车')


# # 方案5:
#
# def inside(group, s,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
# # 形参前加*和**是打包的意思,实参中*和**是解包的意思
# def outer(func):
#     # func=inside
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#     return wrapper
#
# inside=outer(inside)
# inside('蓝色',3,'跑车')

# # 方案6:
#
# def inside(group, s,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
# def recharge(num):
#     for i in range(num,101):
#         time.sleep(0.05)
#         print(f'\r当前电量:{'▋'*i} {i}%',end='')
#     print('电量已充满!')
#
# # 形参前加*和**是打包的意思,实参中*和**是解包的意思
# def outer(func):
#     # func=inside
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#     return wrapper
#
# inside=outer(inside)
# inside('蓝色',3,'跑车')
#
# recharge=outer(recharge)
# recharge(11)

# 方案7:
# def inside(group, s,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
# def recharge(num):
#     for i in range(num,101):
#         time.sleep(0.05)
#         print(f'\r当前电量:{'▋'*i} {i}%',end='')
#     print('电量已充满!')
#     return 100
#
# # 形参前加*和**是打包的意思,实参中*和**是解包的意思
# def outer(func):
#     # func=inside
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         response=func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return response
#     return wrapper
# #
# # inside=outer(inside)
# # inside('蓝色',3,'跑车')
#
# recharge=outer(recharge)
# res=recharge(11)
# print(res)


#
# def count_time(func):
#     # func=inside
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         response=func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return response
#     return wrapper
#
# @count_time   #inside=outer(inside)
# def inside(group, s,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
# @count_time
# def recharge(num):
#     for i in range(num,101):
#         time.sleep(0.05)
#         print(f'\r当前电量:{'▋'*i} {i}%',end='')
#     print('电量已充满!')
#     return 100

# 形参前加*和**是打包的意思,实参中*和**是解包的意思

#
# inside=outer(inside)
# inside('蓝色',3,'跑车')

# recharge=outer(recharge)
# res=recharge(11)
# print(res)
#
# inside=outer(inside())
# recharge=outer(recharge)
#
# inside('蓝色',3,'跑车')
# recharge(50)


# from functools import  wraps
#
# def auth(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         # wrapper.__name__=func.__name__
#         # wrapper.__doc__=func.__doc__
#         name=input('请输入账号: ' ).strip()
#         pwd=input('请输入密码: ').strip()
#         if name == 'jack' and pwd == '<演示密码>':
#             res=func(*args,**kwargs)
#             return res
#         else:
#             print('账号或者密码错误! ')
#     return wrapper
# @auth
# def hello(x):
#     """这是主页"""
#     time.sleep(2)
#     print('welcome')
#     return 100
# hello(1)
#
# print(hello.__name__)
# print(hello.__doc__)



# def g_outer(x):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             return res
#         return wrapper
#     return outer
#
# outer=g_outer('张大仙')
#
# @g_outer('李白')
# def hello(x):
#     """这是主页"""
#     time.sleep(2)
#     print('welcome')
#     return 100
# hello(1)

# def auth(source):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             print(f'the log based on {source}')
#             return res
#         return wrapper
#     return outer
# auth(11)
#
#
# @auth('profile')
# def home():
#     name=input('put your name: ').strip()
#     pwd=input('put your pwd: ').strip()
#     if name=='jack' and pwd=='<演示密码>':
#         print('wellcome!')
#     else:
#         print('name or pwd error')
#
# home()



def outer1(func1):
    def wrapper1(*args,**kwargs):
        print('start outer1')
        res=func1(*args,**kwargs)   #func3 = outer2.wrapper
        print('end outer1')
        return res
    return wrapper1

def outer2(x):
    def outer(func2):
        def wrapper2(*args,**kwargs):
            print('start outer2')
            res=func2(*args,**kwargs)    #func2 = outer1.wrapper
            print('end outer2')
            return res
        return wrapper2
    return outer

def outer3(func3):
    def wrapper3(*args,**kwargs):
        print('start outer3')
        res=func3(*args,**kwargs)   #func1 = 原home
        print('end outer3')
        return res
    return wrapper3

#堆栈,先进后出
@outer3
@outer2(10)
@outer1
def home(z):#加载顺序从上到下
    print(z)


home(1)
