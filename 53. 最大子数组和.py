'''给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。'''
'''DP～
设dp[i]表示nums[:i]的最大子数组和，对于每一个nums[i]，需要考虑应该加入前一段子数组，还是开一个新的子数组
若加入前一个子数组，得到dp[i-1]+nums[i]，否则得到nums[i]
边界为，dp[0]=nums[0]，所求为max(dp)'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp, res = nums[0] , nums[0]
        for num in nums[1:] :
            c = max(dp + num, num)
            res = max(c, res)
            dp = c
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [-1,-2]
print(Solution().maxSubArray(nums))