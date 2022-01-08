from typing import List
import collections

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        q = collections.deque()
        q1 = collections.deque()
        q.append([])
        left = collections.defaultdict()
        for num in nums :
            left[num] = left[num]
        print(left)

        return 0

nums = [1,2,2]
print(Solution().subsetsWithDup(nums))