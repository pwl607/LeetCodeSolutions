'''给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。'''
'''设dp[i]=到nums[0...i]的最长连续递增序列长度。加入nums[i]时，若nums[i]>nums[i-1]则dp[i]=dp[i-1]+1，否则dp[i]=1'''

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp0, res = 1, 1
        for i in range(1, len(nums)):
            dp = dp0 + 1 if nums[i] > nums[i-1] else 1
            res = max(res, dp)
            dp0 = dp
        return res

nums = [1,3,5,4,7]
print(Solution().findLengthOfLCIS(nums))