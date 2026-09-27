# 遍历字典默认得到键，再用键读出值。
names = ['张大仙', '李白', '韩信']
for name in names:
    print(name)

# 我遍历字典的键，再根据键取值。
person = {'name': '张大仙', 'age': 18}
for key in person:
    print(key, person[key])

for number in range(3):
    print(number)
