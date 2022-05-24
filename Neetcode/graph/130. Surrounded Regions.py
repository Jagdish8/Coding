https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.vis = [[False for i in range(self.n)] for j in range(self.m)]
        def solve(i,j):
            if(i<0 or j<0 or i>=self.m or j>=self.n or board[i][j] != 'O' or self.vis[i][j]):
                return
            self.vis[i][j] = True
            solve(i+1,j)
            solve(i-1,j)
            solve(i,j+1)
            solve(i,j-1)
        for i in range(self.m):
            if(board[i][0] == 'O' and not self.vis[i][0]):
                solve(i,0)
            if(board[i][self.n - 1] and not self.vis[i][self.n - 1]):
                solve(i,self.n - 1)
        for i in range(self.n):
            if(board[0][i] == 'O' and not self.vis[0][i]):
                solve(0,i)
            if(board[self.m - 1][i] and not self.vis[self.m - 1][i]):
                solve(self.m - 1,i)
        # print(self.vis)
        for i in range(self.m):
            for j in range(self.n):
                if(board[i][j] == 'O' and not self.vis[i][j]):
                    board[i][j] = 'X'