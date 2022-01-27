# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.n = []
        nums = sorted(nums)
        def solve(num,com):
            if(not num):
                if(com not in self.n):
                    self.n.append(com)
                return
            # print(num)
            solve(num[1:],com+[num[0]])
            solve(num[1:],com)
        solve(nums,[])
        return self.n
        