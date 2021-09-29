'''
字典的一般性用法
'''
from collections import defaultdict
# 一个(k,v)结构的list，即是字典列表，等同于items()
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# 相当于设定字典中的（k,v）结构中v的数据类型
# d = defaultdict(list)

# 字典的一般遍历方式
# items()以列表返回可遍历的(键, 值) 元组数组
# for k, v in d.items():
#     print(k, v)

'''
字典的排序
'''
# 按key排序
d = {(4, 5), (6, 1), (9, 3)}
dict_sort_keys = sorted(d)