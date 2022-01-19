'''幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。解集不能包含重复的子集'''
from typing import List
import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n + 1):
            for x in itertools.combinations(nums,i):
                res.append(list(x))
        return res

nums = [1,2,3]
print(Solution().subsets(nums))