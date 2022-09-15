# https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1

Given an array arr[] denoting heights of N towers and a positive integer K, you have
 to modify the height of each tower either by increasing or decreasing them by K only once.
Find out what could be the possible minimum difference of the height of shortest and
 longest towers after you have modified each tower.
Note: Assume that height of the tower can be negative.

import sys
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        
        arr = sorted(arr)
        ma = arr[-1]
        mi = arr[0]
        ans = ma - mi
        
        for i in range(1,n):
            
            ma = max(arr[n-1]-k,arr[i-1]+k)
            mi = min(arr[0]+k,arr[i]-k)
            
            ans = min(ans,ma-mi)
        
        return ans
        