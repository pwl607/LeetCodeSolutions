'''给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        def gen(seq, x, i):  #已生成序列seq，长度为x，当前处理数字i
            #print(seq)
            if x == k :
                res.append(seq)
                return
            if i > n :
                return            
            gen(seq + [i], x + 1, i + 1)
            gen(seq, x, i + 1)        
        res = []
        gen([],0,1)
        return res

n = 4
k = 2
print(Solution().combine(n,k))