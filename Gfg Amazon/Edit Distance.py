# https://practice.geeksforgeeks.org/problems/edit-distance3702/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions


class Solution:
	def editDistance(self, s, t):
		# Code here
		dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
		
		for i in range(len(t)+1):
		    for j in range(len(s)+1):
		        if(i == 0):
		            dp[i][j] = j
		        elif(j == 0):
		            dp[i][j] = i
	            elif(t[i-1] == s[j-1]):
	                dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[i][j]
