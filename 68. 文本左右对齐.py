from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curWidth = -1       #本行长度，由于每次都要先加空格，而第一个单词前无空格，故初始化为-1
        rowLeft = 0         #本行起点
        cntRow = 0          #本行单词数
        netLengthRow = 0    #本行单词不含空格的长度
        for k in range(len(words)):
            word = words[k]
            curWidth = curWidth + 1 + len(word)  #先考虑本行能否容纳本单词（先加空格，再加本单词）
            if curWidth > maxWidth :  #容不下，结算本行，并将words[k]置为下一行第一个词
                if cntRow == 1 :  #本行只有一个单词，左对齐，补全空格
                    res.append(words[rowLeft] + ' ' * (maxWidth - netLengthRow))
                else :
                    numSpaces = maxWidth - netLengthRow  #本行需要的空格数
                    numPerSpace = numSpaces // (cntRow - 1)  #有n个单词，就有n-1个空需要填空格，计算每个空要填多少
                    moreSpace = numSpaces % (cntRow - 1)  #可能除不尽，那么前几个多加一个空格
                    tmpArr = [numPerSpace + 1 if i < moreSpace else numPerSpace for i in range(cntRow)]
                    tmpres = ''
                    x = 0
                    for i in range(rowLeft, k):
                        tmpres = tmpres + words[i]
                        if i < k - 1 :
                            tmpres = tmpres + ' ' * tmpArr[x]
                        x += 1
                    res.append(tmpres)                
                rowLeft = k    #更新下一行起点索引
                curWidth = len(word)  #更新当前行宽度为len(word)（要将word放进下一行）
                cntRow = 1
                netLengthRow = len(word)
            else :   #容得下
                cntRow += 1
                netLengthRow += len(word)
        if cntRow >= 1 :  #循环结束后，还有最后一行未处理
            tmpres = ''
            for i in range(rowLeft, len(words)):
                tmpres = tmpres + words[i]
                if i < len(words) - 1 :
                    tmpres = tmpres + ' '
            numSpaces =  maxWidth - netLengthRow - (cntRow - 1)
            tmpres = tmpres + ' ' * numSpaces
            res.append(tmpres)
        return res


words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.",
        "Art","is","everything","else","we","do"]
maxWidth = 20

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
