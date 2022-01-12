'''给你一个整数数组nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k)且满足 i < j < k ，使得nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。'''
'''遍历num，在过程中更新最小值num[i]和num[j]，i < j，一旦这样的i和j找到，只要再出现比num[j]更大的num，则返回True'''

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        i, j = nums[0] , 2**31   
        for k in range(n):
            if nums[k] > j :
                return True
            elif nums[k] > i :
                j = nums[k]
            else :
                i = nums[k]
        return False 
        
nums = [2,1,5,0,4,6]
nums = [1,2,3,4,5]
nums = [20,100,10,12,5,13]
print(Solution().increasingTriplet(nums))