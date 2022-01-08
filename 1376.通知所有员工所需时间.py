from typing import List
import  collections
'''
总共有n个人；老大是headID；manager[i]=k说明i归k管；i发通知需要informTime[i]的时间
'''
'''
---------
'''

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''建立tell[i]记录i应该通知谁'''
        tell = [[] for _ in range(n)]
        for i in range(len(manager)):
            if manager[i] != -1 :
                tell[manager[i]].append(i)
        '''BFS，headID是头节点，信息传导本层需要的时间作为深度信息'''
        ans = 0
        q = collections.deque() 
        qd = collections.deque()
        q.append(headID)    #头节点入队
        qd.append(0)        #头节点获得信息需要的时间为0
        while q :
            curID = q.popleft()     #获取通知发出者
            curTime = qd.popleft()  #获取信息传递到curID已花费的时间
            if tell[curID] == [] :   #如果curID是底层，没有下属，比较本路径时间
                ans = max(ans, curTime)
                continue
            for x in tell[curID] :  #curID的下属入队，他们收到消息的时间为curTime + informTime[curID]
                q.append(x)
                qd.append(curTime + informTime[curID])
        return ans

'''---------'''

n = 4
headID = 2 
manager = [3,3,-1,2]
informTime = [0,0,162,914]
print(Solution().numOfMinutes(n, headID, manager, informTime))
