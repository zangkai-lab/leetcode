'''
归类：从场馆之间的关系来看，属于图，从逻辑上来看，逐步回溯信息
'''

from typing import List
import collections
class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> \
            List[int]:
        e = collections.defaultdict(list)
        for x, y in edges:
            e[x].append(y)
            e[y].append(x)
        n = len(finalCnt) + 1
        a = [[1, 0]]
        for x in finalCnt:
            a.append([0, x])
        for i in range(len(plans) - 1, -1, -1):
            o, k = plans[i]
            if o == 1:
                a[k][0] *= 2
                a[k][1] *= 2
            elif o == 2:
                for x in e[k]:
                    a[x][0] -= a[k][0]
                    a[x][1] -= a[k][1]
            elif o == 3:
                for x in e[k]:
                    a[x][0] += a[k][0]
                    a[x][1] += a[k][1]
        u, v = 0, 0
        for x, y in a:
            u += x
            v += y
        u = (totalNum - v) // u
        return [x * u + y for x, y in a]