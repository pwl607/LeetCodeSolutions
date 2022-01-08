from typing import List
'''对于当前的[l,r]，在当中插入m，那么[l,m]和[m+1,r]中至少有一个是有序的
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            #print(l,m,r)
            if nums[m] == target :
                return m
            if l == r :
                break
            if nums[l] <= nums[m]:   #[l,m]是有序的
                if nums[l] <= target <= nums[m] :  #若target在[l,m]中，则搜索范围变为[l,m]，否则[m+1,r]
                    r = m 
                else :
                    l = m + 1
            else :      #若[l,m]不是有序的，则[m+1,r]必然有序
                if nums[m+1] <= target <= nums[r]:
                    l = m + 1
                else :
                    r = m
        return -1

nums = [4,5,6,7,0,1,2]
target = 6
print(Solution().search(nums, target))
