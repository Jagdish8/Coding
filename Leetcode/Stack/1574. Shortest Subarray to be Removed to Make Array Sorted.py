# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# Return the length of the shortest subarray to remove.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        def lowerbound(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                
                if arr[mid] == target:
                    right = mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        N = len(arr)
        i = 0
        while i + 1 < N and arr[i] <= arr[i+1]:
            i += 1
        
        if i == N - 1:
            return 0
        j = N - 1
        while j - 1 >= 0 and arr[j] >= arr[j-1]:
            j -= 1
        
        if j == 0:
            return N - 1
        
        result = min(N - (N - j), N - i -1)
        
        for k in range(i+1):
            l = lowerbound(j, len(arr), arr[k])
            result = min(result, l - (k + 1))
        return result