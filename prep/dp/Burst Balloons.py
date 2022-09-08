# https://leetcode.com/problems/burst-balloons/


# TLE O(N2**N)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        self.memo = {}
        
        def solve(nums):
            
            # print(self.memo)
            if(tuple(nums) in self.memo):
                # print("hiiii")
                # print(self.memo)
                return self.memo[tuple(nums)]
            
            if(len(nums) == 1):
                return nums[0]
            
            max_coins = 0
            for i in range(len(nums)):
                if(i == 0):
                    gain = 1*nums[i]*nums[i+1] + solve(nums[i+1:])
                elif(i == len(nums)-1):
                    gain = nums[i-1]*nums[i]*1
                else:
                    gain = nums[i-1]*nums[i]*nums[i+1] + solve(nums[:i]+nums[i+1:])
                max_coins = max(max_coins, gain)
            self.memo[tuple(nums)] = max_coins
            return max_coins
            
        return solve(nums)
        # return self.memo[nums]