'''累加数 是一个字符串，组成它的数字可以形成累加序列。
一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
给你一个只包含数字'0'-'9'的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def judge(num1:int, num2:int, numResidual:str) -> bool :   #给定前两个数，判断numResidual是不是累加串（numResidual=从num中扣除num1和num2的剩余串）
            a, b, c = num1, num2, num1 + num2
            s = numResidual
            while s :
                #print(a,b,c,s)
                sc = str(c)
                if s[:len(sc)] == sc :   #s开头为c
                    s = s[len(sc):]
                    a = b
                    b = c
                    c = a + b
                else :
                    return False
            return True

        n = len(num)        
        for i in range(1, n-1):
            for j in range(i+1, n):
                s1 = num[:i]
                s2 = num[i:j]
                s3 = num[j:]
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0') or (len(s3) > 1 and s3[0] == '0') :  #去掉含先导0的情况
                    continue
                if judge(int(s1), int(s2), s3) :
                    return True
        return False

num = '199100199'
num = '112358'
num = '101'
print(Solution().isAdditiveNumber(num))