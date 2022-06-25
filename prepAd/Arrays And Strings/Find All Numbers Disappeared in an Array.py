# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        while(i < len(nums)):
            # print(i,nums)
            if(i+1 != nums[i] and nums[nums[i]-1] != nums[i]):
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
            else:
                i += 1
        
        ans = []
        
        for i, j in enumerate(nums):
            if(i+1 != j):
                ans.append(i+1)
            
        return ans


# swap sort
                 
        