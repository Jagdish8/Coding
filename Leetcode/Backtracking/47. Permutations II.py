# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

 class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.a = []
        def solve(num,com):
            if(not num and com not in self.a):
                self.a.append(com)
                return
            for i in range(len(num)):
                solve(num[:i]+num[i+1:],com+[num[i]])
        solve(nums,[])
        return self.a