
# i - d
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=0
        
        cur = [0 for i in range(len(matrix[0]) + 1)]
        prev = [0 for i in range(len(matrix[0]) + 1)]
        
        for i in range(1,len(matrix)+1):
            # print(cur)
            for j in range(1,len(matrix[0])+1):
                            
                if(matrix[i-1][j-1]=="1"):
                    cur[j]=min(cur[j-1],prev[j],prev[j-1])+1
            m = max(m,max(cur))
            # print(cur)
            prev = cur
            cur = [0 for i in range(len(matrix[0]) + 1)]  # imp

        return m*m        


# 2 - d
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         m=0
        
#         dp=[[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
#         for i in range(1,len(matrix)+1):
#             print(dp[i])
#             for j in range(1,len(matrix[0])+1):
#                 if(matrix[i-1][j-1]=="1"):
#                     dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
#                     m=max(dp[i][j],m)
#             print(dp[i])

#         return m*m        
