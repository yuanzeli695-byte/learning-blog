# deepcopy 会递归复制嵌套的可变容器。
import copy

original = ['张大仙', ['李白', '韩信']]
copied = copy.deepcopy(original)
copied[1][0] = '杜甫'
print(original)
print(copied)
