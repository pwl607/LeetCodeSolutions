from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix :
            return []
        
        res = []
        i, j, cnt, d = 0, 0, 0, [0,1]
        m, n = len(matrix), len(matrix[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def turn(d):
            if d == [0,1]:
                return [1,0]
            if d == [1,0]:
                return [0,-1]
            if d == [0,-1]:
                return [-1,0]
            if d == [-1,0]:
                return [0,1]

        def inGrid(x,y) -> bool :
            if x >= 0 and x < m and y >=0 and y < n :
                return not vis[x][y]
            else :
                return False

        while cnt < m * n :
            res.append(matrix[i][j])
            cnt += 1
            vis[i][j] = True
            if inGrid(i + d[0], j + d[1]):
                i += d[0]
                j += d[1]
            else :
                d = turn(d)
                i += d[0]
                j += d[1]

        return res

matrix = [[1,4],
          [5,8],
          [9,12]]
print(Solution().spiralOrder(matrix))