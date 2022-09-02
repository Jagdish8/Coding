# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapify(h)
        for i in nums:
            heappush(h,i)
            if(len(h)>k):
                heappop(h)
        # print(h)
        return h[0]

# using min heap
# notes