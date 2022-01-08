class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        res = ['']
        for x in p :
            if x == '' or x == '.' :
                continue
            if x == '..' :
                if len(res) > 1 :
                    res.pop()
            else :
                res.append(x)

        q = ''
        for x in res :
            q = q + x + '/'
        if len(q) > 1 :
            q = q[:len(q)-1]
        return q


path = '/a/./b/../..////c///'
path = '/home//foo/'
#path = '/../'
print(Solution().simplifyPath(path))