'''给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。你可以假设数组是非空的，并且给定的数组总是存在多数元素。'''
'''投票法。想象开始一场投票选举，数组中的元素是每个选民支持的对象，最后当选的一定是众数。
每个人依次投票。若当前无候选人，则当前得票人成为候选人；若当前有候选人，若当前投票人要选的是该候选人，则他的计票+1，否则-1，如果候选人的计票为0，则下台。'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        candidate, cnt = 0, 0
        for num in nums :
            if cnt == 0 :
                candidate = num
            if candidate == num :
                cnt += 1
            else :
                cnt -= 1
        return candidate

nums = [2,2,1,1,1,1,1,2,2]
print(Solution().majorityElement(nums))