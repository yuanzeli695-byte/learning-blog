# is 比较对象身份，不比较内容是否相等。
left = ['a', 'b']
right = ['x', 'y']
left.append(right)
right.append(left)
print(left[2] is right)
print(right[2] is left)
