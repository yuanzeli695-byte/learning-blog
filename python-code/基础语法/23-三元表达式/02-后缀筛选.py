# endswith 判断结尾，append 收集符合条件的名称。
names = ["康师傅_老坛酸菜", "统一_老坛酸菜", "白象_原味"]
selected = []

for name in names:
    if name.endswith("老坛酸菜"):
        selected.append(name)

print(selected)  # ['康师傅_老坛酸菜', '统一_老坛酸菜']
