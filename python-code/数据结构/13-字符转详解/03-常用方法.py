# 这些方法都会返回结果，不会原地修改字符串。
print('ABcd'.lower(), 'ABcd'.upper())
names = ['李白', '杜甫', '白居易']
print('-'.join(names))
print('李白-杜甫-白居易'.replace('-', ':', 1))
print('84'.isdigit(), '8.a4'.isdigit())
