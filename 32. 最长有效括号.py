'''使用一个栈，遇到 ( 入栈，遇到 ) 且栈顶有 ( 则出栈，有效括号长度为连续成功出栈次数*2'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        cur , maxcur = 0, 0
        for st in s :
            print(stack)
            if st == '(':
                stack.append(st)
            else :      #遇到 ) 判断是否可以操作出栈
                if stack :  #栈非空，可以出栈
                    stack.pop()
                    cur += 1
                else :   #栈已空，不能出栈，结算当前累计的操作
                    maxcur = max(cur, maxcur)
                    print(cur, maxcur)
                    cur = 0
        return maxcur * 2
    

s = ")()(())))"
s = ''
s = "((()(((()())"
print(Solution().longestValidParentheses(s))