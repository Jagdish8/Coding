https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        # h = {}
        vis = [False for i in range(len(nums))]
        def solve(index):
            if(index<0 or index >= len(nums) or vis[index]):
                return False
            if(nums[index] == 0):
                return True
            vis[index] = True
            return solve(index+nums[index]) or solve(index-nums[index])
        return solve(start)
        