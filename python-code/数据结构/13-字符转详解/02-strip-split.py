# 我先清理字符串，再比较从左和从右拆一次。
name = '  张大仙  '
print(name.strip())
names = '李白-杜甫-白居易-陶渊明'
print(names.split('-', 1))
print(names.rsplit('-', 1))
