# 拆开每个二元组，过滤后组成名称到价格的映射。
products = [("康师傅_老坛酸菜", 5), ("统一_老坛酸菜", 6), ("白象_原味", 8)]
prices = {name: price for name, price in products if not name.startswith("康师傅")}

print(prices)  # {'统一_老坛酸菜': 6, '白象_原味': 8}
