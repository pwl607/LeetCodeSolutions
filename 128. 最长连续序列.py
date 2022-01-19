'''给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。'''
from typing import List

'''先去重，然后遍历数组元素num。
若num-1在数组中，num不会是最长序列的开头，跳过
否则，尝试以num开头构建连续序列，不断检验num+1是否在数组中，更新长度'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums :
            if not num - 1 in nums :
                k = num + 1
                cur_length = 1
                while k in nums :
                    cur_length += 1
                    k += 1
                res = max(res, cur_length)
        return res

nums = [100,4,200,1,3,2,5,7,6,8]
print(Solution().longestConsecutive(nums))
