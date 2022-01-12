'''给你一个由候选元素组成的集合 candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates 中的每个元素在每个组合中只能使用一次 。注意：解集不能包含重复的组合'''

from typing import List
import collections

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = collections.Counter(candidates)  #预处理：统计candidates中每个数的出现次数
        candidates = list(set(candidates))  #candidates去重
        res = []

        def work(seq, sumNow, k):  #seq 已选的序列，sumNow 当前已产生序列的和，k 当前处理candidates[k]
            #print(seq, sumNow, k)            
            if sumNow == target :  #已产生和为target的序列
                nonlocal res
                res.append(seq)
                return
            if sumNow > target :   #已超过，剪枝
                return
            if k >= len(candidates):
                return
            for i in range(freq[candidates[k]] + 1):  #枚举当前的candidates[k]用几次
                work(seq + [candidates[k]] * i, sumNow + candidates[k] * i, k + 1)

        work([], 0 , 0)
        return res

candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates, target))