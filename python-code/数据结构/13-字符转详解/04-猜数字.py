# isdigit 对负号和小数点会返回 False。
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
