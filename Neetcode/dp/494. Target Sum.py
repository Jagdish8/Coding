https://leetcode.com/problems/target-sum/

class Solution:    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target)
        if(target > sum(nums)):
            return 0
        target = sum(nums)-target
        if(target % 2):
            return 0
        target = target//2
        dp = [[0 for i in range(target+1)] for j in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if(j >= nums[i-1]):
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]