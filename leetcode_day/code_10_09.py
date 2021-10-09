from typing import List
from sortedcontainers import SortedDict
import collections

'''
@time: 10月09日
@question: 352. 将数据流变为多个不相交区间
@analysis: 去重+长序列的处理 or 有序映射维护区间+二分查找确定区间位置
'''
#
# class SummaryRanges:
#
#     def __init__(self):
#         self.array = []
#
#     def addNum(self, val: int) -> None:
#         self.array.append(val)
#
#     def getIntervals(self) -> List[List[int]]:
#         ans = []
#          使用list(set()) 对于列表进行去重
#         my_array= list(set(self.array))
#         temp = sorted(my_array)
#         num = 0
#         longth = len(temp)
#         if longth == 1:
#             ans.append([temp[0],temp[0]])
#          对于长序列的处理，可以分多种情况来处理结尾的不确定性
#         for i in range(1,longth):
#             if temp[i-1] + 1 == temp[i] and i != longth-1:
#                 num += 1
#             elif temp[i-1] + 1 != temp[i] and i != longth-1:
#                 ans.append([temp[i-1]-num,temp[i-1]])
#                 num = 0
#             elif temp[i-1] + 1 == temp[i] and i == longth-1:
#                 num += 1
#                 ans.append([temp[i]-num,temp[i]])
#             elif temp[i-1] + 1 != temp[i] and i == longth-1:
#                 ans.append([temp[i-1]-num,temp[i-1]])
#                 ans.append([temp[longth-1],temp[longth-1]])
#         return ans

class SummaryRanges:

    def __init__(self):
        # 字典排序，这就是结果哈
        self.intervals = SortedDict()

    # 每加入一个数都动态的维护这么一个字典
    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        # 找到 l1 最小的且满足 l1 > val 的区间 interval1 = [l1, r1]
        # 如果不存在这样的区间，interval1 为 len(intervals)
        interval1 = intervals_.bisect_right(val)
        # 找到 l0 最大的且满足 l0 <= val 的区间 interval0 = [l0, r0]
        # 在有序集合中，interval0 就是 interval1 的前一个区间
        # 如果不存在这样的区间，interval0 为尾迭代器
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            # 情况一
            return
        else:
            left_aside = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_aside = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_aside and right_aside:
                # 情况四
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_aside:
                # 情况二
                intervals_[keys_[interval0]] += 1
            elif right_aside:
                # 情况三
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                # 情况五
                intervals_[val] = val

    def getIntervals(self) -> List[List[int]]:
        # 这里实际上返回的是 List[Tuple[int, int]] 类型
        # 但 Python 的类型提示不是强制的，因此也可以通过
        return list(self.intervals.items())



