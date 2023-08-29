# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while(i < len(nums)):
            if(nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]):
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(len(nums)):
            if(nums[i] != i + 1):
                ans.append(i + 1)
        return ans