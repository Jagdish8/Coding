# https://leetcode.com/problems/next-permutation/

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of
#  arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater
#  permutation of its integer. More formally, if all the permutations of the array are
#   sorted in one container according to their lexicographical order, then the next permutation
#    of that array is the permutation that follows it in the sorted container. If such arrangement
#     is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in
#      ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have
#  a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

# https://www.youtube.com/watch?v=LuLCLgMElus&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=10

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(not nums or len(nums) == 1):
            return
        
        n = len(nums)
        index1 = n - 2
        
        while(index1 >=0 and nums[index1] >= nums[index1 + 1]):
            index1 -= 1
        
        if(index1 >= 0):
            index2 = n - 1
            while(index2 > index1 and nums[index2] <= nums[index1]):
                index2 -= 1
            self.swap(index1,index2,nums)
            
        self.reverse(index1 + 1, n-1, nums)
        
    def swap(self, a , b, nums):
        nums[a],nums[b] = nums[b],nums[a]
    
    def reverse(self,a,b,nums):
        while(a<b):
            self.swap(a,b,nums)
            a += 1
            b -= 1