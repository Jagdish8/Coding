# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(not nums):
            return 0
        if(len(nums) == 1):
            return max(nums)
        
        nums[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            nums[i] = max(nums[i]+nums[i-2],nums[i-1])
            
        return nums[-1]