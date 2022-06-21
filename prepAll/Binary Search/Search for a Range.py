# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binS(arr,target,flag):
            low = 0 
            high = len(nums)-1
            res = -1
            while(low <= high):
                mid = low + (high-low)//2
                if(nums[mid] == target):
                    res = mid
                    if(flag):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif(nums[mid] > target):
                    high = mid - 1
                else:
                    low = mid + 1
            return res
        left = binS(nums,target,True)
        right = binS(nums,target,False)
        return [left,right]

# first find the leftmost occurance of target
# rightmost
                    
        