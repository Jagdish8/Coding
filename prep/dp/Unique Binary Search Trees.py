# https://leetcode.com/problems/unique-binary-search-trees/

# https://www.youtube.com/watch?v=ox7fOk3HjlA

class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = {}
        
        def solve(n):
            if(n <= 1):
                return 1
            if(n in self.dp):
                return self.dp[n]
            ans = 0
            for i in range(1,n+1):
                ans += solve(i-1)*solve(n-i)
            self.dp[n] = ans
            return ans
        
            
        return solve(n)