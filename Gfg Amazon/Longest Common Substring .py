# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):

		# Code here
		dp = [[0 for i in range(m+1)] for j in range(n+1)]
		res = 0
		for i in range(n+1):
		    for j in range(m+1):
		        if(i == 0):
		            dp[i][j] = 0
		        elif(j == 0):
		            dp[i][j] = 0
	            elif(S1[i-1] == S2[j-1]):
	                dp[i][j] = 1 + dp[i-1][j-1]
	                res = max(dp[i][j],res)
                else:
                    dp[i][j] = 0
        return res