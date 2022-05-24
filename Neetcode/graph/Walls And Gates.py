https://www.codingninjas.com/codestudio/problems/walls-and-gates_1092887?leftPanelTab=0

def wallsAndGates(a, n, m):
    for i in range(n):
        for j in range(m):
            if(a[i][j] == 2147483647):
                a[i][j] = min(solve(a,i,j,n,m,[]),a[i][j])  
    return a
def solve(a,i,j,m,n,vis): # vis important to save time
    if(i<0 or j<0 or i>=m or j>=n or a[i][j] == -1 or [i,j] in vis):
        return 2147483647
    if(a[i][j] == 0): #found gate
        return 0
    if(a[i][j] != 2147483647):  # important to save time
        return a[i][j]
    return min(1+solve(a,i+1,j,m,n,vis + [[i,j]]),1+solve(a,i,j+1,m,n,vis + [[i,j]]),1+solve(a,i-1,j,m,n,vis + [[i,j]]),1+solve(a,i,j-1,m,n,vis + [[i,j]]))