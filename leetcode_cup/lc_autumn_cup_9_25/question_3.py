
'''
归类：从场馆之间的关系来看，属于图，从逻辑上来看，逐步回溯信息
其中最重要的逻辑是怎么代换x，就是设立一个矩阵，将x作为1,仅仅计算x的个数，其实含义早已确定
'''

from typing import List
import collections

class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> \
            List[int]:
        # 建立value默认数据结构为list的字典
        e = collections.defaultdict(list)
        # 将该字典用邻接关系填充
        for x, y in edges:
            e[x].append(y)
            e[y].append(x)
        # 第一个使用1填充，剩下的都使用[0,x]填充:有什么意义呢？
        a = [[1, 0]]
        for x in finalCnt:
            a.append([0, x])
        # 使用倒序遍历
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
        # 绝妙的运算方法：使用第一维来替代x的计算，得出x的个数
        u, v = 0, 0
        for x, y in a:
            u += x
            v += y
        u = (totalNum - v) // u
        return [x * u + y for x, y in a]