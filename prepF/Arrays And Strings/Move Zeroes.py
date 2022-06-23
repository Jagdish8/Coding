# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i,j in enumerate(nums):
            if(j != 0):
                nums[i],nums[zero] = nums[zero],nums[i]
                zero += 1


# eg :  [0,1,0,3,12]
# zero = 0

# at index 0
# 0 != 0 False
# [0,1,0,3,12]
# zero = 0

# at index 1
# 1 != 0
# nums[1] = 0
# nums[0] = 1
# [1,0,0,3,12]
# zero = 1

# at index 2
# 0 != 0 False
# zero = 1
# [1,0,0,3,12]

# at index 3
# 3 != 0
# nums[3] = 0
# nums[1] = 3
# [1,3,0,0,12]
# zero = 2

# at index 4
# 12 != 0
# nums[4] = 0
# nums[2] = 12
# [1,3,12,0,0]
        