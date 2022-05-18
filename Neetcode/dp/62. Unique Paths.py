https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.d = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if(m == 1 or n == 1):
            return 1
        if((m,n) in self.d):
            return self.d[(m,n)]
        self.d[(m,n)] = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
        return self.d[(m,n)]