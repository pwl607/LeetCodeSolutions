'''实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。'''

'''生成方法，找到下标i<j，nums[i] < nums[j]，交换两数可得到一个“更大的排列”'''
'''要保证是“下一个排列”，要让i尽可能大，nums[j]尽可能小'''
'''要实现i尽可能大，可从右向左找i，找到第一个满足nums[i]<nums[i+1]的i即可'''
'''要实现nums[j]尽可能小，在找到i后，从右向左扫描，找到第一个满足nums[j]>nums[i]的j'''
'''交换i,j，交换后nums[i+1 :]必为降序，将其反转为升序'''
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1 :    #没有找到i，说明nums本身是降序的，已是最大排列
            nums.sort()  #恢复到从小到大排列即可
        else :
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            left , right = i + 1, n - 1
            while left < right :
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1




nums = [1,2,3,4,7,6,5]
Solution().nextPermutation(nums)
print(nums)