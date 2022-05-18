https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if(i==0):
                    dp[i][j] = 0
                elif(j == 0):
                    dp[i][j] = 1
                elif(j>=coins[i-1]):
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j]