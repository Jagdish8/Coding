# https://leetcode.com/problems/increasing-triplet-subsequence/

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

#with extra space (O(N),O(3))
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        s = []
        for i in nums:
            if(not s):
                s.append(i)
            else:
                if(len(s) > 2):
                    return True
                if(i>s[-1]):
                    s.append(i)
                else:
                    pos = self.findPos(i,s)
                    s[pos] = i
            if(len(s) > 2):
                return True
        return False
    
    
    def findPos(self,target,s):
        
        # find first number which is greater than target
        
        l = 0
        h = len(s)-1
        res = 0
        while(l <= h):
            m = l + (h-l)//2
            if(s[m] == target):
                return m
            elif(s[m] > target):
                res = m
                h = m - 1
            else:
                l = m + 1
        return res

# without extra space (O(N),O(1))
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif first_num <= n <= second_num:
                second_num = n
            else:
                return True
        return False
