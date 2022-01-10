from typing import List

'''用单调栈快速求出每个大于nums2[i]的第一个元素'''
'''从后向前遍历nums2，对每个元素，先将栈中不小于它的元素全部出栈，栈顶即是第一个大于nums[i]的元素；再将nums[i]入栈'''
'''此操作可以保证，每个nums2[i]入栈时，栈中剩余的都是nums2[i]开始的严格递增序列'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2) :  
            while stack and num >= stack[-1] :
                stack.pop()
            res[num] = stack[-1] if stack else -1 
            stack.append(num)
        return [res[num] for num in nums1]
    
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1, nums2))