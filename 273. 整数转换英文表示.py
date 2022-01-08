class Solution:
    def numberToWords(self, num: int) -> str:
        single = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        teen = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        ten = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        sep = ['','Thousand', 'Million','Billion']    #2**31约21.4亿，不到Trillion
        
        def work2(s:str) -> str:   #处理两位或一位数s，s是字符串
            if s == '0' or s == '00' :
                return ''
            if len(s) == 2 :
                if s[0] == '1':
                    return teen[int(s[1])]
                else :
                    return ten[int(s[0])] + single[int(s[1])]
            else :
                return single[int(s[0])]

        def work(s: str) -> str :  #处理三位数s，s是字符串
            if s == '000' :
                return ''
            if len(s) == 3 :  #三位数满的
                if s[0] == '0':  #第一位为0
                    return work2(s[1] + s[2])
                return single[int(s[0])] + 'Hundred' + work2(s[1] + s[2])
            else :
                return work2(s) 

        if num == 0 :
            return 'Zero'
        res = ''
        numStr = str(num)
        k = len(numStr) - 1
        j = 0
        while k >= 0 :
            cur = work(''.join(reversed(numStr[k::-1][:3])))
            if cur != '':
                res = cur + sep[j] + res
            k -= 3
            j += 1
        
        res = list(res)
        k = 1
        while k < len(res):
            if res[k] != res[k].lower() :
                res.insert(k, ' ')
                k += 2
            else :
                k += 1
        return ''.join(res)

num = 9101202303

print(Solution().numberToWords(num))
