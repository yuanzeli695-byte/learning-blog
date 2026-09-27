# 我分别观察嵌套列表和扁平列表的结果。
more = ['梵音天', '玄净天']
nested = ['李兴云']
flat = ['李兴云']
nested.append(more)
flat.extend(more)
print(nested)
print(flat)
