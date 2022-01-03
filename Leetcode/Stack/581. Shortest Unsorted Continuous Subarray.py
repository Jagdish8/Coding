# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

 class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def binarySearch1(m,arr):
            l = 0
            h = len(arr) - 1
            while(l<=h):
                mid = (l+h)//2
                if(arr[mid] > m):
                    h = mid - 1
                else:
                    l = mid + 1
            return (h + 1)
        def binarySearch2(m,arr):
            l = 0
            h = len(arr) - 1
            while(l<=h):
                mid = (l+h)//2
                if(arr[mid] >= m):
                    h = mid - 1
                else:
                    l = mid + 1
            return (h + 1)
        n = len(nums)
        if(n == 0 or n == 1):
            return 0
        i = 1
        while(i<n):
            if(nums[i-1]>nums[i]):
                i = i - 1
                break
            i = i + 1
        j = n - 2
        while(j>-1):
            if(nums[j]>nums[j+1]):
                j = j + 1
                break
            j = j - 1
        if(i == n):
            return 0
        mi = min(nums[i:j+1])
        ma = max(nums[i:j+1])
        lindex = binarySearch1(mi,nums[0:i])
        rindex = binarySearch2(ma,nums[j+1:]) + j
        print(lindex,rindex)
        return rindex - lindex + 1