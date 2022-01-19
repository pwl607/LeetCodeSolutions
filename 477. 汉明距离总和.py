from typing import List
'''取出每个数的某一二进制位，统计出0的数量x（1的数量n-x）'''
'''例如[4,14,2] = [0100, 1110, 0010]'''

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        taker = 1   #通过 n & taker 取出 n 的二进制某一位，taker = 1, 2, 4, ...
        n = len(nums)
        res = 0
        for _ in range(30):
            x = 0
            for num in nums :
                if num & taker == 0 :
                    x += 1
            res += x * (n - x)
            taker *= 2
        return res


nums = [4,14,4]
print(Solution().totalHammingDistance(nums))