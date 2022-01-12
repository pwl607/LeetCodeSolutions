'''若从x出发能到y，但不能到y+1，说明[x...y]中任意一点出发都不能到y+1。因为如果存在一点x<=k<=y可以到y+1，那么就存在x -> k -> y+1的走法，产生矛盾'''
'''从0出发尝试走完全程，若中间遇到x不能到达，就以x为起点进行尝试，一趟遍历即可'''

from typing import List

'''#1 不断尝试起点
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tried = [False for _ in range(n)]   #记录加油站是否作为起点尝试过
        start, g, i = 0, 0, 0    #start 当前尝试起点位置；g 汽油余量
        tried[0] = True
        while True:            
            print('当前位于'+str(i)+'  油量'+str(g))
            nextIndex = 0 if i == n - 1 else i + 1   #下一站的编号
            if g < 0 :   #进站时，检查油量，若小于0说明到不了本站，重置本站为起点
                if tried[i] :  #本站已尝试过，返回-1，否则陷入死循环
                    return -1
                else :
                    start = i
                    tried[i] = True
                    g = gas[i]
            else :
                g += gas[i]   #可以到达，在本站加油
            
            g = g - cost[i]   #开往下一站
            i = nextIndex
            
            if g >= 0 and i == start :
                return start
'''

#2 更新起点：从某个点出发，遇到不能到达的站，计算油的缺口，并向前推起点，看能不能补足缺口
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        def nextStation(i):
            return 0 if i == n - 1 else i + 1
        
        def lastStation(i):
            return n - 1 if i == 0 else i - 1

        n = len(gas)
        start, g, i = 0, 0, 0   #start 起点；g 剩余油量

        while True :
            g = g + gas[i] - cost[i]    #开往下一站
            i = nextStation(i)

            if g < 0 :   #进站后油量不足，abs(g)就是油的缺口
                start = lastStation(start)
                g = g + gas[start] - cost[start]
                while g < 0 :
                    start = lastStation(start)
                    g = g + gas[start] - cost[start]
                    if start == i :  #倒推起点已尝试到了当前位置i
                        return start if g >=0 else -1

            elif i == start :       #可以到达下一站
                return start
                



gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

#gas = [2,3,4]
#cost = [3,4,3]
print(Solution().canCompleteCircuit(gas, cost))