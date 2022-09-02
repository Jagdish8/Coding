# https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        
        # 1-d
        dp = [0 for i in range(budget + 1)]
        
        for i in range(1,len(present)+1):
            for j in range(budget,-1,-1):
                if(j >= present[i-1]):
                    dp[j] = max(dp[j],future[i-1]-present[i-1] + dp[j-present[i-1]])
            
        return dp[-1]
        
        # 2-d
        dp = [[0 for i in range(budget + 1)] for j in range(len(present) + 1)]
        
        for i in range(1,len(present)+1):
            for j in range(budget + 1):
                
                if(j >= present[i-1]):
                    dp[i][j] = max(dp[i-1][j],future[i-1]-present[i-1]+dp[i-1][j-present[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
            
        return dp[i][j]
        