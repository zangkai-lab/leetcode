from typing import List
import collections
'''
@time: 10月08日
@question: 187.重复的DNA序列
@analysis: 搜索 匹配
'''

# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         ans = []
#         my_dict = {}
#         # a[x:y]用法：注意是左闭右开
#         for i in range(len(s)-10):
#             if s[i:i+10] not in my_dict:
#                 my_dict[s[i:i+10]] = 1
#             else:
#                 my_dict[s[i:i + 10]] += 1
#             if my_dict[s[i:i + 10]] == 2:
#                 ans.append(my_dict[s[i:i + 10]])
#         return ans

# leetcode
# 定义全局变量，习惯好
L = 10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        # 将所有value填为0，避免了一次搜索加一次判断加一次赋值
        cnt = collections.defaultdict(int)
        # 注意range是右开的，需要加一
        for i in range(len(s) - L + 1):
            # 后面多次使用直接定义，避免多次运算
            sub = s[i : i + L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

