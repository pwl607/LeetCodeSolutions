'''从cards中选cnt项，使和为偶数，且最大；若能，输出这个最大值，否则输出0'''
'''定义状态dp(k,x,odd/even)=从0..k牌中选x张，且和为偶数或奇数，可得到的最大的和,odd=奇 even=偶
    状态转移 k-1 -> k 的若干情况
    1. cards[k]为奇数odd，若选这张牌，dp(k, x, odd) = dp(k-1, x-1, even) + cards[k]， dp(k, x , even) = dp(k-1, x-1, odd) + cards[k]
    2. cards[k]为奇数odd，不选这张牌，dp(k, x, odd) = dp(k-1, x, odd), dp(k, x, even) = dp(k-1, x, even)
    3. cards[k]为偶数even，选这张牌，dp(k, x, odd) = dp(k-1, x-1, odd) + cards[k], dp(k, x, even) = dp(k-1, x-1, even) + cards[k]
    4. cards[k]为偶数even，不选这张牌，dp(k, x, odd) = dp(k-1, x, odd), dp(k, x, even) = dp(k-1, x, even)
    总结方程：
        cards[k]为奇数时，dp(k, x, odd) = max(dp(k-1, x-1, even) + cards[k], dp(k-1, x, odd))
                        dp(k, x, even) = max(dp(k-1, x-1, odd) + cards[k], dp(k-1, x, even))
        cards[k]为偶数时，
    边界：
        只考虑第一张，若不选第一张则和是0，即dp[0][0][..] = 0
        若要选第一张，若card[0]是奇数，则dp[0][1][odd] = cards[0]，否则cards[0][1][even] = cards[0]

    问题所求即：dp(n, cnt, even)
    '''

from typing import List
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        
        return 0

'''从cards中选cnt项，使和为偶数，且最大；若能，输出这个最大值，否则输出0'''
cards = [ 1,2,8,9]
cnt = 3
print(Solution().maxmiumScore(cards, cnt))