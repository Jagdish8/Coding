https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.h = []
        self.vis = {}
        self.r = len(grid)
        self.c = len(grid[0])
        self.k = 0
        for i in range(self.r):
            for j in range(self.c):
                if(grid[i][j] == 1):
                    self.h.append([i,j])
                    self.vis[(i,j)] = False
        self.count = 0
        def solve(x,y):
            if(x<0 or y<0 or x>=self.r or y>=self.c or grid[x][y] == 0 or self.vis[(x,y)]):
                return
            self.k += 1
            self.vis[(x,y)] = True
            solve(x+1,y)
            solve(x-1,y)
            solve(x,y+1)
            solve(x,y-1)
        for i in self.h:
            if(not self.vis[(i[0],i[1])]):
                solve(i[0],i[1])
                self.count = max(self.count,self.k)
                self.k = 0
        return self.count