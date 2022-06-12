https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        lastpo=n-1
        for i in range(n-2,-1,-1):
            if(i+nums[i]>=lastpo):
                lastpo=i
        if(lastpo==0):
            return True
        else:
            return False