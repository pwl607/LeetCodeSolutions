'''计算pow(x,n)，x为浮点数，n为整数（可能是0或负数）'''
'''一般的算法，需要n-1次运算，每次乘x，计算路径x -> x^2 -> x^3 -> ... ->x^n'''
'''容易想到，每次的乘数可以更新，x -> x^2 -> x^4 -> ... 但这样只能得到2^k次方的结果'''
'''因此可以将n分解为2^k之和，例如10 = 0 + 2 + 0 + 8，那计算x^10的路径就是x (x) -> x^2 (x^2) -> x^2 (x^4) -> x^10 (x^8)'''
'''括号里的是乘数，每次更新乘数，但只在需要时更新计算结果'''
'''分解n的方法之一，使用二进制，10 = (1010)，只需不断取出最后一位，即可判断当前需不需要纳入计算结果'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(x,n):
            res = 1.0
            cs = x     #初始乘数为x
            while n > 0 :
                if n % 2 != 0 :  #末尾不为0，需纳入计算结果
                    res *= cs
                n //= 2
                cs *= cs  #更新乘数
            return res
        return quickPow(x, n) if n >= 0 else 1.0/quickPow(x, -n)


x = 0.5
n = -2
print(Solution().myPow(x, n))