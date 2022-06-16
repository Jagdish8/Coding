# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

class Solution:
    def binarySearch(self,nums,target):
        # print(nums)
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low + (high-low)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findIndex(nums)
        left = self.binarySearch(nums[:minIndex],target)
        right = self.binarySearch(nums[minIndex:],target)
        if(left != -1):
            return left
        if(right == -1):
            return -1
        return minIndex + right
    def findIndex(self,nums):
        if(nums[0] <= nums[-1]):
            return 0
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = low + (high-low)//2
            if(nums[mid-1]>nums[mid]):
                return mid
            if(nums[mid]>nums[mid+1]):
                return mid+1
            elif(nums[mid] >= nums[low]):
                low = mid + 1
            else:
                high = mid - 1

# first find the index where minimum value is present
# from that index to right will be sorted and from start till that index will sorted
# use binary search to search