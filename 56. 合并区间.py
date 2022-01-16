'''以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x:x[0])  #将区间按左端点升序排列
        for x in intervals :
            if not res or x[0] > res[-1][1] :
                res.append(x)
            else :
                res[-1][1] = max(res[-1][1], x[1])
        return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))