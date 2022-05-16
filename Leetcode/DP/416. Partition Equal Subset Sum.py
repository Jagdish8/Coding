class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s %2):
            return False
        s = s//2
        dp = [[False for i in range(s+1)] for j in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(s+1):
                if(j == 0):
                    dp[i][j] = True
                elif(i==0):
                    dp[i][j] = False
                elif(j>=nums[i-1]):
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j]
        