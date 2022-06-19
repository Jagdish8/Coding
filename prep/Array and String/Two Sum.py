# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,j in enumerate(nums):
            r = target - j
            if(r in h):
                return [h[r],i]
            else:
                h[j] = i

# idea is if we check for all pairs it'll be be O(n*2)
# but hash table lookup takes O(1) time
# therefore new complexity is O(n)