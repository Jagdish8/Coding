# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


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
        # print(dp)
        return solve(n)


# n = 5

# dp = [-1,-1,-1,-1,-1]

# solve(5)
# dp[4] = solve(3) + solve(2) = solve(3) + 2

# solve(3)
# dp[3] = solve(1) + solve(2) = 1 + 2 = 3

# dp[4] = 3 + 2 = 5
