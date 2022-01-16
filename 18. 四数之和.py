'''给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
'''

'''先将nums排序，规定a<b<c<d，枚举a和b，对于确定的a,b，在剩余部分找c和d'''
'''开始c=b+1, d=n-1，若nums[c]+nums[d]<t (t=target-nums[a]-nums[b])，则c右移，否则d左移'''
'''每次移动都要保证取到与上次不同的元素'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4 :
            return []
        nums.sort()
        res = []

        a, b = 0, 1
        while a <= n - 4 :
            while b <= n - 3 :         
                c = b + 1
                d = n - 1
                t = target - nums[a] - nums[b]
                while c < d :
                    if nums[c] + nums[d] == t :
                        res.append([nums[a], nums[b], nums[c], nums[d]]) #发现解，c和d同时移动
                        cnext = c + 1
                        while cnext < d and nums[cnext] == nums[c]:
                            cnext += 1                            
                        c = cnext
                        dnext = d - 1
                        while dnext > c and nums[dnext] == nums[d]:
                            dnext -= 1
                        d = dnext 
                    else :
                        if nums[c] + nums[d] < t :
                            cnext = c + 1
                            while cnext < d and nums[cnext] == nums[c]:
                                cnext += 1                            
                            c = cnext
                        else :
                            dnext = d - 1
                            while dnext > c and nums[dnext] == nums[d]:
                                dnext -= 1
                            d = dnext                
                #更新b
                bnext = b + 1
                while bnext <= n - 3 and nums[bnext] == nums[b]:
                    bnext += 1
                b = bnext                
            anext = a + 1
            while anext <= n - 4 and nums[anext] == nums[a]:
                anext += 1
            a = anext
            b = a + 1
        return res

nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(Solution().fourSum(nums, target))