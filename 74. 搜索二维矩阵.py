'''编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。'''

'''将矩阵展开成一维数组查找（长度 = m * n）'''
'''数组的第k个元素还原为矩阵下标 k = i*n + j  ->  i = k // n , j = k - i * n '''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])  #m行n列
        left, right = 0, m * n - 1
        while left <= right :
            mid = (left + right) // 2
            #print(left,mid,right)
            i = mid // n
            j = mid - i * n 
            if matrix[i][j] == target :
                return True
            if matrix[i][j] < target :
                left = mid + 1
            else :
                right = mid - 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1,1]]
target = 3
print(Solution().searchMatrix(matrix, target))