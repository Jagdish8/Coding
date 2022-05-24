https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        q = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    q.append([i,j])
        while(q):
            # print(q)
            q1 = []
            for i in q:
                if(i[0]+1 < m and grid[i[0]+1][i[1]] == 1):
                    q1.append([i[0]+1,i[1]])
                    grid[i[0]+1][i[1]] = 2
                if(i[0]-1 >= 0 and grid[i[0]-1][i[1]] == 1):
                    q1.append([i[0]-1,i[1]])
                    grid[i[0]-1][i[1]] = 2
                if(i[1]+1 < n and grid[i[0]][i[1]+1] == 1):
                    q1.append([i[0],i[1]+1])
                    grid[i[0]][i[1]+1] = 2
                if(i[1]-1 >= 0 and grid[i[0]][i[1]-1] == 1):
                    q1.append([i[0],i[1]-1])
                    grid[i[0]][i[1]-1] = 2
            count += 1
            q = q1
        # print(grid)
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    return -1
        if(count == 0):
            return 0
        return count - 1
        