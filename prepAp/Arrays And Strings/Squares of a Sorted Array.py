# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for i in  nums]
        i = 0
        j = len(nums) - 1
        index = len(nums) - 1
        while(index >= 0):
            if(abs(nums[i]) <= abs(nums[j])):
                res[index] = nums[j]*nums[j]
                j -= 1
            else:
                res[index] = nums[i] * nums[i]
                i += 1
            index -= 1
        return res
        