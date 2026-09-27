# 分支从上往下执行，顺序会影响结果。
grade = 59
if grade == 100:
    print('满分')
elif grade >= 80:
    print('表现很好')
elif grade >= 60:
    print('及格')
else:
    print('需要继续练习')
