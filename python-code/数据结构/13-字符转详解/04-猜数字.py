# 我只接受纯数字字符，猜中 36 后结束循环。
target = 36
while True:
    text = input('猜一个数字：').strip()
    if not text.isdigit():
        print('请输入非负整数')
        continue
    guess = int(text)
    if guess > target:
        print('猜大了')
    elif guess < target:
        print('猜小了')
    else:
        print('猜中了')
        break
