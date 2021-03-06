'''
n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：
每个整数都在范围 [0, 2**n - 1] 内（含 0 和 2**n - 1）
第一个整数是 0
一个整数在序列中出现 不超过一次
每对 相邻 整数的二进制表示 恰好一位不同 ，且
第一个 和 最后一个 整数的二进制表示 恰好一位不同
给你一个整数 n ，返回任一有效的 n 位格雷码序列 。

输入：n = 2
输出：[0,1,3,2]
解释：
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 00 和 01 有一位不同
- 01 和 11 有一位不同
- 11 和 10 有一位不同
- 10 和 00 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- 00 和 10 有一位不同
- 10 和 11 有一位不同
- 11 和 01 有一位不同
- 01 和 00 有一位不同
'''

'''
由低位生成高位计算。如n=2的一个解：[00,01,11,10]
前面全部加0，然后翻转，前面全部加1:[00,01,11,10]前加0，翻转成[10,11,01,00]，前面加1，得到
[000,001,011,010,110,111,101,100]，就是n=3的一个解
用字符串处理，最后转化
'''
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:

        if n == 1 :
            return [0,1]
        if n == 2 :
            res = ['00','01','11','10']
        res = ['00','01','11','10']
        for i in range(3, n+1):
            res = res + res[::-1]
            mid = 2**(i-1)
            for k in range(mid):
                res[k] = '0' + res[k]
                res[k+mid] = '1' + res[k+mid]

        ans = []
        for r in res:
            ans.append(int(r,2))
        return(ans)

'''------'''
n = 5
print(Solution().grayCode(n))