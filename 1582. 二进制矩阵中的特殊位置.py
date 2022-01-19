'''给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。
特殊位置定义
如果 mat[i][j] = 1并且第i行和第j列中的所有其他元素均为0，则位置 (i, j) 被称为特殊位置。'''
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])   #m行n列
        rowFlag = [False for _ in range(m)]
        colFlag = [False for _ in range(n)]
        res = 0
        for i in range(m):
            if rowFlag[i] :
                continue
            for j in range(n):
                #检查(i,j)
                if not rowFlag[i] and not colFlag[j] and mat[i][j] == 1:
                    for k in range(n):  #检查本行
                        if k == j :
                            continue
                        if mat[i][k] == 1 :
                            print('Row Check Found ', i, k)
                            rowFlag[i] = True  #本行至少两个1，不必再检查本行
                            colFlag[k] = True
                    for k in range(m): #检查本列
                        if k == i :
                            continue
                        if mat[k][j] == 1 :
                            colFlag[j] = True  #本列至少两个1，不必再检查本列
                            rowFlag[k] = True
                    if not rowFlag[i] and not colFlag[j] :  #行列检查都通过
                        print(i,j)
                        res += 1
                if rowFlag[i] :  #如果本行已确定不存在特殊位置，不再继续检查本行的其他列
                    break
        return res        




mat = [[0,0,0,0,0],
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]

mat = [[0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,1,1,0]]
print(Solution().numSpecial(mat))

