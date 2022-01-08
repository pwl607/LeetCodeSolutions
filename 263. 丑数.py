'''给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数2、3 和/或5的正整数。

认为1也是丑数
'''

'''
依据定义，丑数可以写成 2^x * 3^y * 5^z 的形式。只要不断把2、3、5因子除掉，如果最后只剩下1，就是丑数
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1 :
            return True
        if n <= 0 :
            return False
        dd = [2,3,5]
        for d in dd :
            while n % d == 0 :
                n //= d
        return n == 1

n = 2
print(Solution().isUgly(n))