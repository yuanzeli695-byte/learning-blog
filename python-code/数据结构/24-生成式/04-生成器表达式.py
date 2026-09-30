# 生成器按需产出，不会在创建时把全部结果装进列表。
names = ["康师傅_老坛酸菜", "统一_老坛酸菜", "白象_原味"]
generator = (name for name in names)

print(next(generator))  # 康师傅_老坛酸菜
print(list(generator))  # ['统一_老坛酸菜', '白象_原味']
print(list(generator))  # []：已经耗尽
