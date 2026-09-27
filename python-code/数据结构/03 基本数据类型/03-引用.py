# 我让两个列表互相包含对方，打印一个布尔判断即可。
left = ['a', 'b']
right = ['x', 'y']
left.append(right)
right.append(left)
print(left[2] is right)
print(right[2] is left)
