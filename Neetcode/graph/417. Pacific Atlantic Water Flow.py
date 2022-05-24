https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(row, col,visit, prevVal):
            if (row,col) in visit or row < 0 or col < 0 or row > rows-1 or col > columns-1 or heights[row][col] < prevVal:
                return 
            visit.add((row,col))
            dfs(row-1, col, visit, heights[row][col])
            dfs(row+1, col, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
        for c in range(columns):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, columns-1,atl, heights[r][columns-1])
        res = []
        for i in range(rows):
            for j in range(columns):
                if (i,j) in pac and (i,j) in atl:
                    res.append((i,j))
        return res