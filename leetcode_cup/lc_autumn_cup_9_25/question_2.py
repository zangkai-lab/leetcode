from typing import List
'''
@time: 09月25日
@question: 秋季杯赛题2
@analysis: BFS 地图格状结构 字典加速 维护表格后筛选
@error: 思路
'''

class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
        # 得到场地的长和宽
        n, m = len(terrain), len(terrain[0])
        # 包含初始位置，速度信息的字典
        h = {(position[0], position[1], 1)}
        # 包含初始位置，速度信息的列表
        q = [(position[0], position[1], 1)]
        t = 0
        #
        while t < len(q):
            x, y, v = q[t]
            t += 1
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # 得到四个方向其中一个的坐标
                xx, yy = x + dx, y + dy
                # 当这个坐标在范围内时
                if 0 <= xx < n and 0 <= yy < m:
                    # 得到新的速度
                    vv = v + terrain[x][y] - terrain[xx][yy] - obstacle[xx][yy]
                    rec = (xx, yy, vv)
                    # 符合大于0的条件后更新列表
                    if vv > 0 and rec not in h:
                        h.add(rec)
                        q.append(rec)
        q.sort()
        return [[x, y] for x, y, v in q if ((x != position[0] or y != position[1]) and v == 1)]