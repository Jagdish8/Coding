# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # top-down
        memo = {}
        def solve(nums,remaining):
            
            if(remaining == 0):
                return 1
            if(remaining in memo):
                return memo[remaining]
            res = 0
            for i in range(len(nums)):
                if(remaining - nums[i] >= 0):
                    res += solve(nums,remaining - nums[i])
            memo[remaining] = res
            return memo[remaining]
        return solve(nums,target)
        # return self.ans
                
        # bottom-up
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
        return dp[target]