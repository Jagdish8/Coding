# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[0])-1
        self.ans = 0
        self.d = {}
        if(obstacleGrid[0][0] == 1):
            return 0
        
        def solve(m,n):
            if(m == 0 and n == 0):
                return 1
            if(obstacleGrid[m][n] == 1):
                return 0
            if((m,n) in self.d):
                return self.d[(m,n)]
            if(m == 0):
                self.d[(m,n)] = solve(m,n-1)
            elif(n == 0):
                self.d[(m,n)] = solve(m-1,n)
            else:
                self.d[(m,n)] = solve(m-1,n) + solve(m,n-1)
            return self.d[(m,n)]
        
        return solve(m,n)
        