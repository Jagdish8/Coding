# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        if(n<m):
            return -1
        
        #binary search notes
        low = max(nums)
        high = sum(nums)
        res = -1
        
        
        while(low <= high):
            
            # print(low,high)
            
            mid = low + (high-low)//2
            
            if(self.isvalid(mid,m,nums)):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
            
    def isvalid(self,maximum,m,nums):
        
        count = 1
        s = 0
        for i in nums:
            s += i
            if(s > maximum):
                count += 1
                s = i
            if(count > m):
                return False
        return True


# binary search