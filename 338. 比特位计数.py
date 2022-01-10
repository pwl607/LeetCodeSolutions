'''给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。'''
'''逐个数计算，容易实现O(nlogn)的算法。用动态规划可实现一个O(n)的算法'''
'''设bit[i]为i的二进制1的个数。若存在 0 <= j < i，使j的比特数比i少1，则bit[i] = bit[j] + 1，对每个i，只要能快速找出j，则问题解决'''
'''容易发现，将i的二进制的最高有效位（一定是1）去掉，剩余的部分就是要找的j，如i = 19 (10011)，去掉第一个1就是要找的 j = 3 (0011)'''
'''如何找到j？设一个数k，其二进制只有第一位为1，且长度于i相当，例如i=19，则k =16 (10000)，那么j = i - k，显然k为不超过i的最大2的整数次幂'''
'''判断一个数是不是2的整数次幂的简便方法，若x & (x-1) = 0，则x是二的整数次幂'''
'''在循环中，不断更新k即可'''

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit = [0,1,1]
        k = 2
        if n <= 2 :
            return bit[:n+1]
        for i in range(3, n + 1):
            if i & (i-1) == 0 :
                bit.append(1)
                k = i
            else :
                bit.append(bit[i-k]+1)
        return bit
        

n = 5
print(Solution().countBits(n))