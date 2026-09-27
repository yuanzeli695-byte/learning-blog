# 这里只是循环练习，用的是演示值，不用于真实登录。
demo_user = 'demo'
demo_password = 'demo'
attempts = 0
while attempts < 3:
    name = input('账号：')
    password = input('密码：')
    if name == demo_user and password == demo_password:
        print('演示登录成功')
        break
    attempts += 1
    print('账号或密码不匹配')
else:
    print('三次尝试结束')
