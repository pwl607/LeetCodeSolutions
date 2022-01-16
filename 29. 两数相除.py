'''给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如truncate(8.345) = 8 以及 truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是[-2**31,  2**31 - 1]。本题中，如果除法结果溢出，则返回2**31 - 1。'''
'''要求的z=x/y，满足yz <= x < y(z+1)，可通过二分法查找z，乘法用快速乘（类似快速幂）转化为加法 '''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        #防结果溢出
        minInt , maxInt = - 2 ** 31, 2 ** 31 - 1
        if dividend == minInt :
            if divisor == -1 :
                return maxInt  #当被除数为minInt时，若除数为-1，结果会溢出
            if divisor == 1 :
                return minInt
        if dividend == maxInt :
            if divisor == 1 :
                return maxInt
            if divisor == -1 :
                return -maxInt
        if divisor == minInt :
            return 1 if dividend == minInt else 0
        if divisor == 0 :
            return 0
        
        #预处理负数
        neg = False   #将所有负数变为正数，并用neg（negative）标记改变
        if dividend < 0 :
            dividend = - dividend
            neg = not neg
        if divisor < 0 :
            divisor = - divisor
            neg = not neg
        
        #用加法实现乘法
        def quickAdd(a,b) -> int :
            if b > a :  
                a, b = b, a  #保证 a>b
            if b == 0:
                return a
            res, plus = 0, a
            while b :
                if b & 1 :    #整数&1 -> 取出其二进制的最后1位
                    res += plus
                plus += plus
                b >>= 1
            return res            

        #二分查找
        left, right = 0, maxInt + 1
        while left < right :
            mid = (left + right) // 2
            check = quickAdd(mid, divisor)  #当前试商 * 被除数，与除数比较
            if check <= dividend < check + divisor :  #找到解
                break
            if check > dividend :
                right = mid
            else :
                left = mid
        return - mid if neg else mid


dividend, divisor = 2147483647, 1
print(Solution().divide(dividend, divisor))