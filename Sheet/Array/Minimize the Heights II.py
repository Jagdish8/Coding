# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1

# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and
#  tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower.
#  After the operation, the resultant array should not contain any negative integers.


class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr = sorted(arr)
        ma = arr[-1]
        mi = arr[0]
        ans = ma - mi
        
        for i in range(1,n):
            
            if(arr[i] < k):
                continue
            
            ma = max(arr[n-1]-k,arr[i-1]+k)
            mi = min(arr[0]+k,arr[i]-k)
            
            ans = min(ans,ma-mi)
        
        return ans