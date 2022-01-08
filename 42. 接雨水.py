from typing import List

'''考虑当前位置i，记其左侧最高柱子为leftmax，右侧最高柱子为rightmax，则位置i能容纳的雨水为min(leftmax, rightmax) - height[i]（小于0则为0）'''
'''从左向右扫描确定每个位置的leftmax，从右向左扫描确定每个位置的rightmax'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        for i in range(n - 1) :
            l[i + 1] = max(l[i], height[i])
        for i in range(n-1, 0, -1):
            r[i - 1] = max(r[i], height[i])

        res = 0
        for i in range(n):
            res += max(min(l[i], r[i]) - height[i], 0)
        return res

height = [4,2,0,3,2,5]
print(Solution().trap(height))