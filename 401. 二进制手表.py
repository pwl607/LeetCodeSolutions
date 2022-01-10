from typing import List
import typing


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        #用一个10位二进制数表示每个灯的状态(从上到下，从左到右)
        #如：0110 100100，表示6:36
        #枚举有turnedOn个1的二进制数，返回显示的时间

        def show(c) -> str :  #输入一个整数c，输出对应的时间，若是非法时间输出'x'
            s = bin(c)[2:]    #转化为二进制串
            while len(s) < 10 :
                s = '0' + s   #前补0，补足到10位
            #print(s)
            t1 = int(s[0]) * 8 + int(s[1]) * 4 + int(s[2]) * 2 + int(s[3])
            t2 = int(s[4]) * 32 + int(s[5]) * 16 + int(s[6]) * 8 + int(s[7]) * 4 + int(s[8]) * 2 + int(s[9])
            if t1 >= 12 or t2 >= 60 :
                return 'x'
            else :
                s1 = str(t1)
                s2 = str(t2)
                if len(s2) == 1 :
                    s2 = '0' + s2
                return s1 + ':' + s2
        
        def w(c) -> int :  #计算c的二进制中1的个数（汉明重量）
            res = 0
            while c > 0 :
                if c % 2 :
                    res += 1
                c //= 2
            return res

        res = []
        for x in range(1024):  #尝试1～1023的所有数（10位二进制）
            if w(x) == turnedOn :
                tmp = show(x)
                if tmp != 'x' :
                    res.append(tmp)
        return res

turnedOn = 2
print(Solution().readBinaryWatch(turnedOn))