https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        n = len(nums)
        
        while(i<n):
            if(nums[i] == val):
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        return j