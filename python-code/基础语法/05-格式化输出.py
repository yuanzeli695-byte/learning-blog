# 整理注：格式化示例依次比较 %、str.format 和 f-string。
#1\%

# #%s可以接收任意类型的值,但%d只能接收整值但%d用的很少
# info1='my name is %s,i am from %s'%('广东','张大仙')
# print(info1)
#
# info2='my name is %(name)s, i am from %(hometown)s'%{'hometown':'广1东','name':'张大仙'}
# print(info2)
#
#
# info='my name is %s'%18
# print(info)
# info3='my name is %s'%['a','b']
# print(info3)
# info4='mty name is%s'%{'a':'a','b':'bb'}
#
# print(info4)






#2\format
# info=info1='my name is {},i am from {}'.format('张大仙','广东')
# print(info)

#
# info=info1='my name is {name},i am from {hometown}'.format(name='张大仙',hometown='广东')
# print(info)



#格式化填充
#****开始****
# a='{0:*^10}'.format('start')
# print(a)

#小数精度控制

# b='{num:.2f}'.format(num=3.1415926)
# print(b)

#3\f
# name=input('请输入你的名字' )
# hometown=input('你来自哪里 ')
# info=f'my name is{name},im from {hometown}'
# print(info)
