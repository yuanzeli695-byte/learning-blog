# 先遍历 names，再把满足条件的名称放入新列表。
names = ["康师傅_老坛酸菜", "统一_老坛酸菜", "白象_原味"]
selected = [name for name in names if name.endswith("老坛酸菜")]

print(selected)  # ['康师傅_老坛酸菜', '统一_老坛酸菜']
