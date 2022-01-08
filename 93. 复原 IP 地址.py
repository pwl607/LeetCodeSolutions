'''将s分割成4个数字（类似隔板法，在中间插入3块板子，分成4部分），验证是不是有效IP'''
from typing import List
import itertools

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def checknum(s) -> bool :   #检查数字s（字符串形式）是不是IP地址中的有效数
            if len(s) > 3 :
                return False
            if len(s) > 1 and s[0] == '0' :   #含有先导0
                return False
            if int(s) > 255 :
                return False
            return True

        def check(s1,s2,s3,s4) -> bool :  #检查s1.s2.s3.s4是不是有效IP
            return checknum(s1) and checknum(s2) and checknum(s3) and checknum(s4)
        
        res = []
        for x,y,z in list(itertools.combinations(range(1, len(s)),3)):
            s1 = s[:x]
            s2 = s[x:y]
            s3 = s[y:z]
            s4 = s[z:]
            if check(s1,s2,s3,s4):
                res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return res    

s = "101023"
print(Solution().restoreIpAddresses(s))