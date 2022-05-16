import sys
class Solution:
    def matrixChainMemoised(self,p, i, j):
        if(i >= j):
            return 0
        if(self.dp[i][j] != -1):
            return self.dp[i][j]
        self.dp[i][j] = sys.maxsize
        for k in range(i,j):
            if(self.dp[i][k] != -1):
                t1 = self.dp[i][k]
            else:
                self.dp[i][k] = t1 = self.matrixChainMemoised(p, i, k)
            if(self.dp[k+1][j] != -1):
                t2 = self.dp[k+1][j]
            else:
                self.dp[k+1][j] = t2 = self.matrixChainMemoised(p, k+1, j)
            self.dp[i][j] = min(self.dp[i][j],t1 + t2 + (p[i - 1] * p[k] * p[j]))
        return self.dp[i][j]
    def matrixMultiplication(self,n,p):
        i = 1
        j = n - 1
        self.dp = [[-1 for i in range(101)] for j in range(101)]
        return self.matrixChainMemoised(p, i, j)