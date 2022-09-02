https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        #base condition so that if 1 exists all unwanted value can be replaced with 1
        if 1 not in nums:
            return 1
        
        # replacing unwanted values with 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        for i in range(n): 
            
            a = abs(nums[i])
            nums[a-1] = - abs(nums[a-1])    
            
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            
        return n + 1


# Index as a hash key.

# Data clean up

# First of all let's get rid of negative numbers and zeros since there is no need of them.
# One could get rid of all numbers larger than n as well, since the first missing positive is
# for sure smaller or equal to n + 1. The case when the first missing positive is equal to
# n + 1 will be treated separately.
# What does it mean - to get rid of, if one has to keep
# and hence could not pop unwanted elements out? Let's just replace all these by 1s.

# [1,-1,-2,8,2,4] --> [1,1,1,1,2,4]

# Now there we have an array which contains only positive numbers in a range from 1 to n, 
# and the problem is to find a first missing positive in O(N) time and constant space.

# That would be simple, if one would be allowed to have a hash-map positive number ->
#  its presence for the array.

# Sort of "dirty workaround" solution would be to allocate a string hash_str with n zeros, and 
# use it as a sort of hash map by changing hash_str[i] to 1 each time one meets number i in the array.

# it needs O(N) space complexity as well

# how to solve under O(1) space complexity?

# Let's not use this solution, 
# but just take away a pretty nice idea to use index as a hash-key for a positive number.

# The final idea is to use index in nums as a hash key and sign of the element as a hash value
# which is presence detector.

# For example, negative sign of nums[2] element means that number 2 is present in nums. The positive sign of nums[3]
# element means that number 3 is not present (missing) in nums.

# To achieve that let's walk along the array (which after clean up contains only positive numbers),
# check each element value elem and change the sign of element nums[elem] to negative to mark that
# number elem is present in nums. Be careful with duplicates and ensure that the sign was changed
# only once.