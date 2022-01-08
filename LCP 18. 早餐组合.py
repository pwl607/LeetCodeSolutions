'''从staple和drinks中各选一个数，和不超过x，共有多少选法 (mod 1000000007)'''
from typing import List
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        while staple[-1] > x :
            staple.pop(-1)
        while drinks[-1] > x :
            drinks.pop(-1)
        if len(staple) > len(drinks):
            staple, drinks = drinks, staple
        print(staple, drinks)
        for i in range(1,len(staple) + 1) :
            staple[-i]
        return 0


staple = [10,20,5]
drinks = [5,5,2]
x = 15
print(Solution().breakfastNumber(staple, drinks, x))

