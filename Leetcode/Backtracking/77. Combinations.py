# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        num = [i+1 for i in range(n)]
        def solve(num,com):
            if(len(com)==k):
                self.res.append(com)
                return
            for i in range(len(num)):
                solve(num[i+1:],com+[num[i]])
        solve(num,[])
        return self.res