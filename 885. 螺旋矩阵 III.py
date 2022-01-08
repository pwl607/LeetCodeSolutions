from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        '''移动方向：右下左上'''
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        '''移动步数：右1，下1，左2，上2，右3，下3，…………，每两步+1
        可用一个[1,1,2,2,3,3...]来记录；作为优化，只需记录now和pre'''
        now, pre = 0, 0
        x, y = rStart, cStart   
        i = -1  
        res = [[x,y]]
        visited = 1
        while True :
            i = (i + 1) % 4
            if now == pre :  #步数需要+1
                now += 1
            else :
                pre = now
            #print(now)
            for _ in range(now):
                x += dx[i]
                y += dy[i]
                if now < 10 :
                    print(x,y,now)
                if x >= 0 and x < rows and y >= 0 and y < cols :
                    res.append([x,y])
                    visited += 1
                    if now<10 :
                        print('Found')
                        print(x,y)
                    #print(visited)
                    if visited >= rows * cols :
                        return res
        return res

rows = 1
cols = 4 
rStart = 0
cStart = 0
output = Solution()
print(output.spiralMatrixIII(1, 4, 0, 0))            