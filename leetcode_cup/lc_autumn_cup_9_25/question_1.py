from collections import deque
'''
@time: 09月25日
@question: 秋季杯赛题1
@analysis: BFS 树结构
@error: 没有判断左右节点是否为空
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        # 特例判断
        if not root:
            return 0
        # 建立队列初始化
        search_queue = deque()
        search_queue.append(root)
        ans = []
        # 遍历队列，遍历过程中筛选符合条件的结果
        while search_queue:
            person = search_queue.popleft()
            if person.left is not None:
                search_queue.append(person.left)
            if person.right is not None:
                search_queue.append(person.right)
            if person.val not in ans:
                ans.append(person.val)
        return len(ans)
