# 整理注：涉及写入/删除的练习已禁用，避免照抄运行时更改真实文件。
#字符编码

# 一\CPU、内存、硬盘
# 计算机三大核心硬件

# 二、文本编辑器读取文件的三个步骤
# 1、启动文本编辑器
# 2,把文件内容从硬盘读到内存
# 3,把数据显示到屏幕上


# 三,运行python程序的步骤
# 1、启动python解释器
# 2、把test.py文件内容从硬盘读入内存
# # 3、把文件内容当成pthon语法识别
#
# #
# #
# # #1/打开文件
# open('data/a.txt.py')
# # open(r'data/a.txt.py')
#
# # 加上r之后直接就是原生的字符串
# f=open('data/a.txt.py',mode='rt')
# print(f)
#
# #2.操作文件(读,写)
# res=f.read()
# print()
#
#
# # 3.关闭文件
# # f.close()
#

# #with语法(上下文管理器)with在读完文件数据之后会自己调用.close\
# with open('data/a.txt.py',mode='rt',encoding='utf-8')as f,\
#         open('data/b.txt',mode='rt',encoding='utf-8')as f2:
#     res=f.read()
#     res2=f2.read()
#     print(res,res2)
#
# input_username = input('请输入账号>>>').strip()
# input_password = input('请输入密码>>>').strip()
#
# with open('data/c.txt', mode='rt', encoding='utf-8') as f:
#     username, password = f.read().strip().split('---', 1)
#
# if username == input_username and password == input_password:
#     print('登录成功')
# else:
#     print('账号或密码错误')


#1.只读模式

# input_username = input('请输入账号>>>').strip()
# input_password = input('请输入密码>>>').strip()
# with open('data\\c.txt',mode='rt',encoding='UTF-8')as f:
#     for line in f:
#         # print(line, end='')
#         username,password=line.strip('\n').split('---', 1)
#         if username == input_username and password == input_password:
#             print('登录成功')
#             break
#     else:
#         print('账号或密码错误')


# 2.只写模式
#w模式下,当文件存在并有内容时,会清空文件内容
# 如果文件不存在则直接创建新建文件
# 千万不能用w模式打开比较正要的文件
# with open('data\\c.txt',mode='w',encoding='utf-8')as f:
#     # f.read()报错,不可读
#     f.write('晓看天色暮看云\n')
#     f.write('行也思君坐也思君')

# 3.追加写模式,只能写不能读
# [公开版禁用] with open('data\\d.txt',mode='a',encoding='utf-8')as f:
# [公开版禁用]     # f.read()报错,不能读
# [公开版禁用]     f.write('那么短,还站那么远\n')
# [公开版禁用]     f.write('那么短,还站那么远\n')
# [公开版禁用]     f.write('那么短,还站那么远\n')


# [公开版禁用] import os
# [公开版禁用] with open('data/k.txt',mode='rt',encoding='utf-8')as f,\
# [公开版禁用]     open('data/.k.txt.swap',mode='rt',encoding='utf-8')as f1:
# [公开版禁用]     for line in f:
# [公开版禁用]         res = line.replace('一天','一年')
# [公开版禁用]         f1.write(res)
# [公开版禁用]     os.remove('data/k.txt')
# [公开版禁用]     os.rename('data/.k.txt.swap','data/k.txt')
