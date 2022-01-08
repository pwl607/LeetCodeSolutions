'''
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        vis = [False for _ in range(n)]  #标记是否使用过nums[i]
        res =[]  #最终答案

        def build(perm):  #perm=当前已生成的排列
            if len(perm) == n :  #长度已满，全排列已生成
                res.append(perm)
                return
            for i in range(n) :
                if vis[i] == False :  #在nums中寻找未使用过的元素
                    vis[i] = True
                    build(perm+[nums[i]])
                    vis[i] = False

        build([])
        return res

'''test'''
test = Solution()
nums = [1,2,3]
print(test.permute(nums))
