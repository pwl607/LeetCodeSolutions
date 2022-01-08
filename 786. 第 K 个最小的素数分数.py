'''AC'''
from typing import List
def cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        frac = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                frac.append([arr[i],arr[j]])

        def mycmp(a,b):
            return a[0] * b[1] - a[1] * b[0]
        
        frac.sort(key=cmp_to_key(mycmp))
        return frac[k-1]

'''Input'''
arr = [1,2,3,5] 
#arr = [1,2]
k = 3
'''Output'''
print(Solution().kthSmallestPrimeFraction(arr, k))