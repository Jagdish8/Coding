# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # so far, all the integers that could find their own correct place 
        # have been put to the correct place, next thing is to find out the
        # place that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

# swap sort
