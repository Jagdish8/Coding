def cutRod(price, n):
	dp = [[-1 for i in range(n+1)] for j in range(len(price)+1)]
	for i in range(len(price)+1):
		for j in range(n+1):
			if(j==0):
				dp[i][j] = 0
			elif(i==0):
				dp[i][j] = 0
			elif(j>=i):
				dp[i][j] = max(dp[i-1][j],price[i-1]+dp[i][j-i])
			else:
				dp[i][j] = dp[i-1][j]
	return dp[i][j]