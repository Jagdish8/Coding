import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if(i == 0):
                    dp[i][j] = sys.maxsize
                elif(j==0):
                    dp[i][j] = 0
                elif(i == 1):
                    if(j%coins[i-1]):
                        dp[i][j] = sys.maxsize
                    else:
                        dp[i][j] = j // coins[i-1]
                elif(j >= coins[i-1]):
                    dp[i][j] = min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j] if dp[i][j] != sys.maxsize else -1