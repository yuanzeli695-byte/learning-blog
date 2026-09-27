# 我分别试用 lower、upper、join、replace 和 isdigit。
print('ABcd'.lower(), 'ABcd'.upper())
names = ['李白', '杜甫', '白居易']
print('-'.join(names))
print('李白-杜甫-白居易'.replace('-', ':', 1))
print('84'.isdigit(), '8.a4'.isdigit())
