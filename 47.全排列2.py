'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
输入 nums = [1,1,2]
输出 [[1,1,2],[1,2,1],[2,1,1]]
'''
from cgitb import reset
from typing import List
import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        vis = set()
        for x in itertools.permutations(nums):
            if not x in vis :
                res.append(list(x))
                vis.add(x)
        return res
        
nums = [1,1,2]
print(Solution().permuteUnique(nums))
