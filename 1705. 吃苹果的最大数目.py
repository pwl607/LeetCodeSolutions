'''有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。
在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。
也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。
你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。'''
'''贪心策略，每次都吃最接近腐烂的苹果，借助数据结构堆来实现'''
from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        ans = 0
        heap = []  #heap中的元素是二元组[day,apple]，表示第day天腐烂的苹果有apple个
        '''第一阶段：前n天能吃的苹果'''
        for i in range(n):
            while heap and heap[0][0] <= i :
                heapq.heappop(heap)  #去除已腐烂的苹果
            if apples[i] > 0 :
                heapq.heappush(heap, [i + days[i], apples[i]])
            if heap :
                heap[0][1] -= 1    #heap[0]总是腐烂日期最小的那一堆
                ans += 1
                if heap[0][1] == 0 :
                    heapq.heappop(heap)  #吃完了，去掉
        '''第二阶段：n天之后还能吃多少'''
        i = n
        while heap :
            while heap and heap[0][0] <= i :
                heapq.heappop(heap)
            if not heap :
                break
            p = heapq.heappop(heap)  #取出（未腐烂的）腐烂日最早的苹果堆
            x = min(p[1], p[0] - i)  #这堆苹果里能吃到多少个
            i += x
            ans += x
        return ans




apples = [1,2,3,5,2]
days = [3,2,1,4,2]
print(Solution().eatenApples(apples, days))