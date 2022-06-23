# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# Sliding window only works if all are positive or all are negative or array is sorted(if both negative and positive)

# using prefix sum
# first watch video
# link : https://www.youtube.com/watch?v=20v8zSo2v18

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {0:1}
        preSum = 0
        count = 0
        for i,j in enumerate(nums):
            preSum += j
            if(preSum - k in h):
                count += h[preSum - k]
            if(preSum not in h):
                h[preSum] = 0
            h[preSum] += 1
        return count
            
        
