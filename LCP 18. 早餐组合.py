'''从staple和drinks中各选一个数，和不超过x，共有多少选法 (mod 1000000007)'''
from typing import List
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        ns, nd = len(staple), len(drinks)
        ks, kd = 0, nd - 1
        res = 0
        while ks < ns and kd >= 0 :
            while kd >=0 and staple[ks] + drinks[kd] > x :
                kd -= 1
            res = (res + (kd + 1)) % 1000000007
            ks += 1
        return res


staple = [2,1,1]
drinks = [9,8,5,1]
x = 9
print(Solution().breakfastNumber(staple, drinks, x))

