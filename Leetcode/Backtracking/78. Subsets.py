# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def solve(num,com):
            if(not num):
                self.res.append(com)
                return
            solve(num[1:],com+[num[0]])
            solve(num[1:],com)
        solve(nums,[])
        return self.res