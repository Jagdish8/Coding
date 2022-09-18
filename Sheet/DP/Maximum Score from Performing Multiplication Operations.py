# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
# Return the maximum score after performing m operations.

 

# Example 1:

# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# Example 2:

# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.



class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        self.memo = {}


        # approach 1, TLE
        def solve(nums,multi):
            
            if(not multi):
                return 0
            
            return max((nums[0]*multi[0])+solve(nums[1:],multi[1:]),
                       (nums[-1]*multi[0])+solve(nums[:-1],multi[1:]))
        
        return solve(nums,multipliers)
    
        
        # approach 2, TLE , but correct for other lang
        def solve(x,y):
            
            if(y == len(multipliers)):
                return 0
            
            if((x,y) in self.memo):
                return self.memo[(x,y)]
            
            # print(self.memo,x,y)
            
            a = (nums[x[0]] * multipliers[y]) + solve((x[0]+1,x[1]),y + 1)
            b = (nums[x[1]] * multipliers[y]) + solve((x[0],x[1]-1),y + 1)
                       
            self.memo[(x,y)] = max(a,b)
            return self.memo[(x,y)]
        
        return solve((0,len(nums)-1),0)


        # approach 3, TLE, correct for other lang
        def solve(x,y):
            
            if(y == len(multipliers)):
                return 0
            
            if((x,y) in self.memo):
                return self.memo[(x,y)]
            
            # print(self.memo,x,y)
            
            a = (nums[x] * multipliers[y]) + solve(x + 1,y + 1)
            b = (nums[(len(nums)-1) - (y-x)] * multipliers[y]) + solve(x,y + 1)
                       
            self.memo[(x,y)] = max(a,b)
            return self.memo[(x,y)]
        
        return solve(0,0)


        # approach 4, accepted, lol
        m = len(multipliers)
        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]



        # approach 5, optimised space
        m = len(multipliers)
        n = len(nums)

        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards

            for left in range(op, -1, -1):

                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])

        return dp[0]
        