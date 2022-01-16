'''给你一个整数n，请你帮忙统计一下我们可以按下述规则形成多少个长度为n的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音'a'后面都只能跟着'e'
每个元音'e'后面只能跟着'a'或者是'i'
每个元音'i'后面不能 再跟着另一个'i'
每个元音'o'后面只能跟着'i'或者是'u'
每个元音'u'后面只能跟着'a'
由于答案可能会很大，所以请你返回 模10^9 + 7之后的结果。

输入n = 2
输出10
所有可能的字符串分别是"ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
'''

'''
递归（带记忆）
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        
        tmp = [[-1 for _ in range(n)] for _ in range(5)]  #a-0,e-1,i-2,o-3,u-4
        def cnt(c,x):  
            if x == 0 :
                tmp[c][x] == 1
                return 1
            if c == -1:
                return (cnt(0,x-1) + cnt(1,x-1) + cnt(2,x-1) + cnt(3,x-1) + cnt(4,x-1)) % mod
            
            a = cnt(0, x-1) if tmp[0][x-1] == -1 else tmp[0][x-1]
            e = cnt(1, x-1) if tmp[1][x-1] == -1 else tmp[1][x-1]
            i = cnt(2, x-1) if tmp[2][x-1] == -1 else tmp[2][x-1]
            o = cnt(3, x-1) if tmp[3][x-1] == -1 else tmp[3][x-1]
            u = cnt(4, x-1) if tmp[4][x-1] == -1 else tmp[4][x-1]
         
            if c == 0:  #a后接e
                ans = e % mod
            if c == 1:  #e后接a i
                ans = (a + i) % mod
            if c == 2:  #i后接a e o u
                ans = (a + e + o + u) % mod
            if c == 3:  #o后接i u
                ans = (i + u) % mod
            if c == 4:  #u后接a
                ans = a % mod
            
            tmp[c][x] = ans
            return ans

        return cnt(-1,n)
'''

# 动态规划
# 倒推上一位：若本位是a，上一位可能是eiu；e -> ai；i -> eo；o ->i ；u ->io
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % mod, (dp[0] + dp[2]) % mod, (dp[1] + dp[3]) % mod, dp[2], (dp[2] + dp[3]) % mod)
        return sum(dp) % mod



n = 10
print(Solution().countVowelPermutation(n))