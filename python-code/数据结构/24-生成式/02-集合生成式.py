# 集合只保留不同的元素；排序后再打印，结果更方便比较。
names = ["康师傅_老坛酸菜", "统一_老坛酸菜", "统一_老坛酸菜"]
unique_names = {name for name in names}

print(sorted(unique_names))
print(len(unique_names))  # 2
print(type(unique_names).__name__)  # set
