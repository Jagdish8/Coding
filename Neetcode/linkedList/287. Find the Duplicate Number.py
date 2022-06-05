https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while(i<len(nums)):
            if(nums[i] != i+1 and nums[i] != nums[nums[i]-1]):
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
            else:
                i = i + 1
        for i in range(len(nums)):
            if(nums[i] != i+1):
                return nums[i]
        
