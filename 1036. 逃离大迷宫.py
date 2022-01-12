from typing import List
import collections


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        points = [[source[0], source[1], 0],[target[0], target[1], 1]]
        for b in blocked :
            points.append([b[0],b[1],-1])  #points记录所有的点，并标记起点0，终点1，障碍-1
        
        points.sort(key = lambda x:(x[0]))
        x = 0 if points[0][0] == 0 else 1
        ori = points[0][0]
        for i in range(len(points)):  
            #排序后，进行坐标离散化：
            # 若原来的坐标和上一个相同，离散化后也相同；若原来相差1，则离散化后相差1；
            # 若原来相差大于1，则离散化后相差2，即将中间的多个空行压缩成1行
            if points[i][0] == ori + 1 :
                x += 1
            elif points[i][0] > ori + 1 :
                x += 2
            ori = points[i][0]
            points[i][0] = x
        maxrow = points[-1][0] + 1
        if ori == 999999 :    #判断原先的最后一点是不死在最后一行
            maxrow -= 1
        
        points.sort(key = lambda x:(x[1]))
        x = 0 if points[0][1] == 0 else 1
        ori = points[0][1]
        for i in range(len(points)):
            if points[i][1] == ori + 1 :
                x += 1
            elif points[i][1] > ori + 1 :
                x += 2
            ori = points[i][1]
            points[i][1] = x
        maxcol = points[-1][1] + 1
        if ori == 999999 :
            maxcol -= 1

        #print(points)

        vis = [[False for _ in range(maxcol + 1)] for _ in range(maxrow + 1)]
        for point in points :
            if point[2] == 0 :
                pStart = [point[0], point[1]]
            elif point[2] == 1 :
                pEnd = [point[0], point[1]]
            elif point[2] == -1 :
                vis[point[0]][point[1]] = True

        q = collections.deque()
        q.append(pStart)
        vis[pStart[0]][pStart[1]] = True

        while q :
            cur = q.popleft()
            if cur == pEnd :  #已到达终点
                return True
            i, j = cur[0], cur[1]
            #print(i,j)
            if i + 1 <= maxrow and not vis[i+1][j]:
                vis[i+1][j] = True
                q.append([i + 1, j])
            if j - 1 >= 0 and not vis[i][j-1]:
                vis[i][j-1] = True
                q.append([i, j - 1])
            if j + 1 <= maxcol and not vis[i][j+1]:
                vis[i][j+1] = True
                q.append([i, j + 1])
            if i - 1 >= 0 and not vis[i-1][j]:
                vis[i-1][j] = True
                q.append([i - 1, j])
        return False


blocked = [[0,5], [2,3],[6,3],[1000,2000],[9999,9998],[9999,10000],[9998,9999],[10000,9999]]
blocked = []
source = [1,1]
target = [9999,9999]


blocked = [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
source = [655988,180910]
target = [267728,840949]

blocked = [[0,4],[2,4],[3,1],[3,3],[4,0],[4,2]]
source = [2,2]
target = [7,3]

print(Solution().isEscapePossible(blocked, source, target))