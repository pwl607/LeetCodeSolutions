'''给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。'''

from tkinter import N
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumArr = sum(arr)
        if sumArr % 3 != 0 :
            return False     #如果全部元素和不是3的倍数，必不可能分成3个和相等部分
        else :
            target = sumArr // 3  #记录target，遍历数组并累加，达到target就记录位置
        
        sumArr, cnt = 0, 0
        for num in arr :
            sumArr += num
            if sumArr == target :
                cnt += 1
                sumArr = 0
        
        return cnt >= 3
        

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
arr = [0,2,1,-6,6,7,9,-1,2,0,1]
arr = [0,0,0,0]
print(Solution().canThreePartsEqualSum(arr))