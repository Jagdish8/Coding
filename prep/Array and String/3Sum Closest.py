# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        diff=100000
        a=sorted(nums)
        for i in range(n):
            l=i+1
            r=n-1
            while(l<r):
                s=a[i]+a[r]+a[l]
                if(abs(s-target)<abs(diff)):
                    diff=target-s
                elif(diff==0):
                    return target
                elif(s>target):
                    r-=1
                else:
                    l+=1
        return target-diff

# two pointer