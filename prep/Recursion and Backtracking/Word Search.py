# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.b = [0,0,m,n]
        def solve(i,j,index):
            if(index == len(word)):
                return True
            if(i < self.b[0] or i >= self.b[2] or j < self.b[1] or j >= self.b[3] or board[i][j]!=word[index]):
                return False
            board[i][j] = ""
            if(solve(i,j+1,index+1) or solve(i,j-1,index+1) or solve(i+1,j,index+1) or solve(i-1,j,index+1)):
                return True
            board[i][j] = word[index]
        for i in range(m):
            for j in range(n):
                if(solve(i,j,0)):
                    return True
        return False

# notes