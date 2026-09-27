# split 从左拆，rsplit 从右拆。
name = '  张大仙  '
print(name.strip())
names = '李白-杜甫-白居易-陶渊明'
print(names.split('-', 1))
print(names.rsplit('-', 1))
