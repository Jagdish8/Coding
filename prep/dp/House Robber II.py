# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(nums[0],nums[1])
        return max(self.runnerop(nums[1:]),self.runnerop(nums[:-1]))
    
    def runnerop(self,nums):
        print(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for k in range(2,len(nums)):
            dp[k]=max(dp[k-1],dp[k-2]+nums[k])
        return dp[-1]