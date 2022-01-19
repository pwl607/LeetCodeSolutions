from re import T
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        #将HH:MM形式的时间字符串转化为该时点为当天的第几分钟
        time = [int(timePoints[i][0:2])*60 + int(timePoints[i][3:5]) for i in range(len(timePoints))]
        time.sort()

        #计算两个时间点（以分钟表示）之间的差，注意若差距大于12小时（720分钟，如1:00和14:00），结果应反方向计
        def work(a:int, b:int) -> int:
            c = abs(a-b)
            if c > 720:
                c = 1440 - c
            return c

        #找最小
        res = work(time[0], time[-1])
        if res == 0:
            return 0
        for i in range(len(time)-1):
            if work(time[i], time[i+1]) < res:
                res = work(time[i], time[i+1])
                if res == 0:
                    return 0

        return res

timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))