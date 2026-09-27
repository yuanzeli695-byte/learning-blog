# 整理注：上半部分是注释练习，下半部分含需要输入的猜数字循环。
# # from unittest import result
# #
# # name='zhangdaxian'
# #
# #
# # result=str("['aa','bb']")
# # print(result,type(result))
# #
# # #索引取值
# # info='good day'
# # print(info[0])
# # print(info[4])
# # print(info[-1])
# #
# # #字符串只能按索引取值,不能按索引改值
# #
# # #切片
# # print(info[0:4])#顾头不顾尾
# # print(info[0:20:3])
# # res=info[10:0:-1]
# # res1=info[::-1]
# # print(res)
# # print(res1)
# #
# # #strip去除空格
# # name='  张大仙  '
# # res=name.strip()
# # print(res)
# # res1=name.lstrip()
# # res2=name.rstrip()
# # print(res1)
# # print(res2)
# #
# # name1='+++$&%*^(*(!!!!zhangdaxian.com'
# # res3=name1.strip('+')
# # print(res3)
# # #
# # # #登录案例
# # # input_username=input('请输入账号').strip()
# # # input_password=input('请输入密码').strip()
# # # if input_password=='<演示密码>' and input_username =='<演示账号>':
# # #     print('登录成功')
# # # else:
# # #     print('账号密码不对')
#
#
#
# names = '李白-韩信-luna 孙悟空'
# res=names.split(' ')#split拆分之后变成列表
# res2=names.split('-',1)
# res3=names.split('-',2)
#
# print(res,type(res))
# print(res2,type(res2))
# print(res3,type(res3))
#
# #长度len
# info='good good study , day day uop!'
# long=len(info)
# print(long,type(long))
#
# # #成员运算in和not in
# # print()
from modulefinder import replacePackageMap
from shlex import join

names='李白-杜甫-白居易-陶渊明'
print(names.split('-',1))
print((names.rsplit('-',1)))

#lower,power
msg='ABcd'
print(msg.lower())
print(msg.upper())


#startswith,endswith
print('君不见黄河之水天上来,奔流到海不复回'.endswith('不复回'))
print('君不见黄河之水天上来,奔流到海不复回'.startswith('黄河'))


# join
l=['李白','杜甫','白居易','陶渊明','1']
print('-'.join(l))

#replace
names = '李白-杜甫-白居易-陶渊明'
print(names.replace('-', ':', 2))

#isdigit
print('84'.isdigit())
print('8.a4'.isdigit())

while 1:
    num=input('请输入你猜的数字').strip()
    if num.isdigit():
        num=int(num)
    else:
        print('不准调皮,输入纯数字')
        continue
    if num > 36:
        print('猜大了')
    elif num<36:
        print('猜小了')
    else:
        print('猜中了')
        break
