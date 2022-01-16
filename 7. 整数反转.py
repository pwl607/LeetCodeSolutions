'''给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。'''

class Solution:
    def reverse(self, x: int) -> int:
        
        def judge(x,f) -> bool :  #判断x（以数组传入）是否溢出，f表示是不是负数
            if len(x) < 10 :
                return False
            if len(x) > 10 :
                return True
            maxInt = [['2','1','4','7','4','8','3','6','4','8'],  # 2**31
                     ['2','1','4','7','4','8','3','6','4','7']]   # 2**31 - 1
            k = 0 if f else 1
            for i in range(10):
                if x[i] < maxInt[k][i]:  #有一位比maxint对应位置小，就不会溢出，无需继续判断
                    return False
                elif x[i] > maxInt[k][i]:
                    return True
            return False
        
        neg = False
        if x < 0 :   #负数特殊处理
            x = -x
            neg = True
        s = list(str(x)[::-1])  #用字符串进行反转
        while s and s[0] == '0':
            s.pop(0)    #去前导0
        if not s :
            s = ['0']
        if judge(s,neg):
            return 0
        else :
            d = int(''.join(s))
            return -d if neg else d
        

    
x = 0
print(Solution().reverse(x))