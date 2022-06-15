# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
#         Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


        def solve(i,j):
            # print(i,j)
            if(i<0 or i>=self.m or j<0 or j>=self.n or grid[i][j] != '1' or vis[i][j]):
                return
            vis[i][j] = True
            solve(i+1,j)
            solve(i-1,j)
            solve(i,j-1)
            solve(i,j+1)
        self.m = len(grid)
        self.n = len(grid[0])
        self.ans = 0
        vis = [[False for i in range(self.n)]for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if(grid[i][j] == '1' and not vis[i][j]):
                    self.ans += 1
                    solve(i,j)
        return self.ans


# easy dfs approach
        