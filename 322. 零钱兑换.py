from typing import List
import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        coins.sort() 
        qs = collections.deque()
        qd = collections.deque()
        if coins[0] <= amount :  #头部入队
            qs.append(0)
            qd.append(0)
        while qs :
            s_cur = qs.popleft()
            d_cur = qd.popleft()
            if s_cur > amount :
                continue
            if s_cur == amount :
                return d_cur
            for coin in coins :
                if s_cur + coin > amount :
                    break
                if s_cur + coin == amount :
                    return d_cur + 1
                else:
                    qs.append(s_cur + coin)
                    qd.append(d_cur + 1)        
        return -1


test = Solution()
coins = [1,2,5]
amount = 100
print(test.coinChange(coins, amount))



