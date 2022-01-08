'''AC'''
'''
给你n个盒子，每个盒子的格式为[status, candies, keys, containedBoxes]，其中：

状态字status[i]：整数，如果box[i]是开的，那么是 1，否则是 0。
糖果数candies[i]: 整数，表示box[i] 中糖果的数目。
钥匙keys[i]：数组，表示你打开box[i]后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。
内含的盒子containedBoxes[i]：整数，表示放在box[i]里的盒子所对应的下标。
给你一个initialBoxes 数组，表示你现在得到的盒子，你可以获得里面的糖果，也可以用盒子里的钥匙打开新的盒子，还可以继续探索从这个盒子里找到的其他盒子。

请你按照上述规则，返回可以获得糖果的 最大数目。
'''
from typing import List
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def work(i) -> bool:
            '''处理i号盒子，返回是否成功打开了盒子'''
            nonlocal candynum
            #print(candynum, i)
            if status[i] == 1 or (status[i] == 0 and havekey[i]):  #盒子是开的或者有钥匙
                nonlocal vis
                vis[i] = True
                
                candynum += candies[i]  #获得糖果
                if keys[i] != []:  #盒子里有钥匙
                    for k in keys[i]:
                        havekey[k] = True  #获得钥匙
                if containedBoxes[i] != []:  #盒子里有其他盒子
                        for k in containedBoxes[i]:
                            initialBoxes.append(k)  #获得盒子
                return True
            else:
                return False

        n = len(status)
        candynum = 0   #可获得的糖果总数
        havekey = [False for _ in range(n)]  #havekey[i]=是否拥有i号盒子的钥匙
        vis = [False for _ in range(n)]     #是否已打开了i号盒子
        tried = [False for _ in range(n)]   #是否尝试失败过

        i = 0
        while i < len(initialBoxes):
            if not work(initialBoxes[i]) :  #没能打开盒子，放到最后，稍后再试
                if not tried[initialBoxes[i]]:
                    tried[initialBoxes[i]] = True
                    initialBoxes.append(initialBoxes[i])
            i += 1

        return candynum

'''Input'''
status = [1,0,1,0]
candies = [7,5,4,100] 
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]

'''Output'''
print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))