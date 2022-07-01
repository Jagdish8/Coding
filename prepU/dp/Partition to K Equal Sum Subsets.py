# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if(sum(nums)%k):
            return False
        
        nums = sorted(nums, reverse = True)
        
        target = sum(nums)//k
        
        if(nums[0] > target):
            return False
        
        vis = ["0"]*len(nums)
        h = {}
        
        def solve(current_sum,k,index):
            
            val = "".join(vis)
            
            # print(val,h)
            
            if(val in h):
                return h[val]
            
            if(k == 0):
                h[val] = True
                return True
            
            if(current_sum == target):
                h[val] = solve(0,k-1,0)
                return h[val]
            
            for i in range(index,len(nums)):
                
                if(vis[i] == "1" or current_sum+nums[i] > target):
                    continue
                    
                vis[i] = "1"
                val = "".join(vis)
                h[val] = solve(current_sum + nums[i], k ,index + 1)
                if(h[val]):
                    return True
                vis[i] = "0"
                
            h[val] = False
            return False
            
            
        return solve(0,k,0)
        