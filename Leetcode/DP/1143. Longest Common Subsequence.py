class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        #memoization
#         self.h = {}
#         def solve(s1,s2,i,j):
#             if((i,j) in self.h):
#                 return self.h[(i,j)]
#             if(i == len(s1) or j == len(s2)):
#                 return 0
#             elif(s1[i] == s2[j]):
#                 self.h[(i,j)] = 1 + solve(s1,s2,i+1,j+1)
#             else:
#                 self.h[(i,j)] = max(solve(s1,s2,i+1,j),solve(s1,s2,i,j+1))
#             return self.h[(i,j)]
#         return solve(text1,text2,0,0)
    
        
        #bottom up
        
        t = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if(i == 0 or j==0):
                    t[i][j] = 0
                elif(s1[i-1] == s2[j-1]):
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[i][j]