# https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


# https://www.youtube.com/watch?v=FWAIf_EVUKE

class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        
        for i in range(9):
            for j in range(9):
                if(grid[i][j] == 0):
                    for val in range(1,10):
                        if(self.isvalid(grid,i,j,val)):
                            grid[i][j] = val
                            if(self.SolveSudoku(grid)):
                                return True
                            grid[i][j] = 0
                    return False
        return True
        
    def isvalid(self,grid,r,c,val):
        
        for i in range(9):
            
            if(grid[i][c] == val):
                return False
            if(grid[r][i] == val):
                return False
            if(grid[3*(r//3) + i//3][3*(c//3) + i%3] == val):
                return False
        return True