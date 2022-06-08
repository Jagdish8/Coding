https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for i in board:
            h = {}
            for j in i:
                # print(h)
                if(j in h and j != "."):
                    return False
                h[j] = 1
        # print("hi")
        #col
        for i in range(9):
            h = {}
            for j in range(9):
                if(board[j][i] in h and board[j][i] != "."):
                    return False
                h[board[j][i]] = 1
        #3*3 
        r = 0
        c = 0
        count = 1
        while(count <= 9):
            # print(r,c)
            h = {}
            for i in range(r,r+3):
                for j in range(c,c+3):
                    # print(h,i,j,board[i][j])
                    if(board[i][j] in h and board[i][j] != "."):
                        # print(board[i][j],i,j)
                        return False
                    h[board[i][j]] = 1
            count = count + 1
            if(count%3 == 1):
                c = 0
                r = r + 3
            else:
                c = c + 3
        return True

        #better approach to check 3*3

        # def nine(board,i,j):
        #     a=[]
        #     for k in range(i,i+3):
        #         for l in range(j,j+3):
        #             if(board[k][l] not in a):
        #                 if(board[k][l] != "."):
        #                     a.append(board[k][l])
        #             else:
        #                 return 0
        #     return True

        # res=True
        # for i in range(0,7,3):
        #     for j in range(0,7,3):
        #         res=(res and nine(board,i,j))
        # return res
        