# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[1 for i in range(n)] for j in range(n)]
        m = n 
        k = l = 0
        val = 1
        
        while(k<m and l<n):
            for i in range(l,n):
                ans[k][i] = val
                val += 1
                # res.append(matrix[k][i])
            k+=1
            for i in range(k,m):
                ans[i][n-1] = val
                val += 1
                # res.append(matrix[i][n-1])
            n-=1
            if(k<m):
                for i in range(n-1,(l-1),-1):
                    ans[m-1][i] = val
                    val += 1
                    # res.append(matrix[m - 1][i])
                m -= 1
            if(l<n):
                for i in range(m-1,k-1,-1) :
                    ans[i][l] = val
                    val += 1
                    # res.append(matrix[i][l])
                l += 1
        
        return ans
        