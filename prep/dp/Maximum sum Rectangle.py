# https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1

# https://www.youtube.com/watch?v=mKluyW4YFvs

import sys
class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        # compresing col wise
        ans = -sys.maxsize
        for cstart in range(C):
            temp = [0]*R
            for cend in range(cstart,C):
                for x in range(R):
                    temp[x] += M[x][cend]
                ans = max(ans,self.kadane(temp))
        return ans
                    
    def kadane(self,arr):
        cs = arr[0]
        ms = arr[0]
        for i in range(1,len(arr)):
            cs = max(arr[i],cs+arr[i])
            ms = max(ms,cs)
        return ms

# (O(R*C^2))
        
