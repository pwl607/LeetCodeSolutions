'''给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。'''

from typing import List

'''设dp[i]表示达到台阶i的最低花费。要达到台阶i，可以从i-1或i-2爬过来。
若从i-1过来，dp[i] = dp[i-1] + cost[i-1]
若从i-2过来，dp[i] = dp[i-2] + cost[i-2]
边界条件，dp[0] = dp[1] = 0'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = 0, 0
        for i in range(2, len(cost)+1):
            dp = min(dp1 + cost[i-1], dp2 + cost[i-2])
            dp2, dp1 = dp1, dp
        return dp


cost = [1,100,1,1,1,100,1,1,100,1]
#cost = [10,15,20]
print(Solution().minCostClimbingStairs(cost))