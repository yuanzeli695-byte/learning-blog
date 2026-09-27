# 整理注：下面的演示账号/密码只用于循环练习，不要用于真实系统。
# num=0
# while num < 10:
#     print(num)
#     num +=1
#
# print('循环结束了')



# while True:
#     info=input('qingshuruneirong')
#     print(info)
#

# while 1:
#     10+10
#     print(1)



username='1'
password='1'
# input_username=input('账号')
# input_password=input('密码')
#
# if username == input_password and password == input_password:
#     print('通过')
# else:
#     print('用户名或者密码输入错误')




num=0
while num<3:
    input_username = input('请输入你的账号 ')
    input_password = input('请输入你的密码 ')
    if input_username == username and input_password == password:
        print('登录成功')
        while True:
            action = input('请输入你的操作 ')
            if action == 'Q':
                break
            print(f'正在齐{action}')
        break
    else:
        print('用户名或密码错误')
        num+=1
else:
    print('账号已经连续3次登录失败,账户已经被锁定')
#



# num=0
# while num<10:
#     if num == 4:
#         num+=1
#         continue#break
#     print(num)
#     num+=1
# else:
#     print('循环正常结束')
#
