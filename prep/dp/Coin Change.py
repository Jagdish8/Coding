# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0



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
                        