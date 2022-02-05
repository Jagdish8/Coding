# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
# Example 2:

# Input: n = 1
# Output: 1

class Solution:
    def countArrangement(self, n: int) -> int:
        a = [i for i in range(1,n+1)]
        self.res = set()
        def solve(com,num,index):
            # print(com,num)
            if(len(com) == n):
                self.res.add(com,)
                return
            for i in range(len(num)):
                if((num[i] % index == 0) or (index % num[i] == 0)):
                    # print(num[i],index)
                    solve(com+(num[i],),num[:i]+num[i+1:],index+1)
        solve((),a,1)
        print(self.res)
        return len(self.res)