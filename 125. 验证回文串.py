'''给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，我们将空字符串定义为有效的回文串。'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def check(c) -> bool:   #c是字母或数字才返回True
            return 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90 or 48 <= ord(c) <= 57

        if not s :
            return True
        i, j = 0, len(s) - 1
        while i < j :
            while not check(s[i]):
                i += 1
                if i > j :
                    break
            if i > j :
                break
            while not check(s[j]):
                j -= 1
                if j < i :
                    break
            if j < i :
                break
            if s[i].lower() != s[j].lower() :
                return False
            i += 1
            j -= 1
        return True

       

s = 'A man, a plan, a canal: Panama'
s = 'A!!!!!!!s!!4!s!!!a'
print(Solution().isPalindrome(s))

