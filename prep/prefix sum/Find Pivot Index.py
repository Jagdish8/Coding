# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        leftSum = 0
        
        for i,j in enumerate(nums):
            if(leftSum == s-leftSum-j):
                return i
            leftSum += j
        return -1