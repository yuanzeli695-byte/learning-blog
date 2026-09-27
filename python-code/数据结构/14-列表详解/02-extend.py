# 两份独立列表避免前一次操作干扰对比。
more = ['梵音天', '玄净天']
nested = ['李兴云']
flat = ['李兴云']
nested.append(more)
flat.extend(more)
print(nested)
print(flat)
