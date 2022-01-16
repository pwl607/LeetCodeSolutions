'''给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        i, j, d = 0, 0, [0,1]
        visited = 0

        def inBoard(i,j) -> bool:
            return i >= 0 and i < m and j >= 0 and j < n and not vis[i][j]
        
        while visited < m * n :
            vis[i][j] = True
            res.append(matrix[i][j])
            visited += 1

            if not inBoard(i + d[0], j + d[1]):
                d = [d[1], -d[0] if d[1] == 0 else 0]  #转向
            i += d[0]
            j += d[1]

        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))