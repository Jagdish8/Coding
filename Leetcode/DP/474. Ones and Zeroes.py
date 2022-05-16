class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.h = {}
        def solve(arr,m,n,l):
            if(l == 0):
                return 0
            if(m == 0 and n == 0):
                return 0
            if((m,n,l) in self.h):
                return self.h[(m,n,l)]
            if(arr[l-1].count("0") <= m and arr[l-1].count("1")<=n):
                self.h[(m,n,l)] = max(1+solve(arr,m-arr[l-1].count("0"),n-arr[l-1].count("1"),l-1),solve(arr,m,n,l-1))
            else:
                self.h[(m,n,l)] = solve(arr,m,n,l-1)
            return self.h[(m,n,l)]
        return solve(strs,m,n,len(strs))
    
        