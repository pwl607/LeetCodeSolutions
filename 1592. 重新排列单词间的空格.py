import numbers


class Solution:
    def reorderSpaces(self, text: str) -> str:
        numSpaces = text.count(' ')  #数空格
        words = text.split()         #提取单词
        if len(words) > 1 :
            x, y = numSpaces // (len(words) - 1), numSpaces % (len(words) - 1)
        else :
            x, y = 0, numSpaces
        res = ''
        for i in range(len(words)):
            res = res + words[i]
            if i < len(words) - 1 :
                res = res + ' ' * x 
            else :
                res = res + ' ' * y 
        return res

text = "  this   is  a sentence "
print(Solution().reorderSpaces(text))