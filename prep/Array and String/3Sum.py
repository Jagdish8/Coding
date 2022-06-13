# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for k in range(len(nums)):
            i = k+1
            j = len(nums)-1
            while(i<j):
                if(nums[i]+nums[j]+nums[k] == 0):
                    ans.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
                elif(nums[i]+nums[j]+nums[k] > 0):
                    j -= 1
                else:
                    i += 1
        return ans

# basic 2 pointer approach