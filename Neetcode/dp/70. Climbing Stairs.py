class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n)]
        def solve(n):
            if(n<3):
                return n
            if(dp[n-1] != -1):
                return dp[n-1]
            dp[n-1] = solve(n-1)+solve(n-2)
            return dp[n-1]
        return solve(n)