

from typing import List
import heapq   #堆(heap)操作

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        n1, n2 = len(nums1), len(nums2)
        
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, n1))]  #三元组:nums1[i]+nums2[j], i, j
        while pq and len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

        return res

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))