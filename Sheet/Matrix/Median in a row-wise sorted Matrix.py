# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

# Example 1:

# Input:
# R = 3, C = 3
# M = [[1, 3, 5], 
#      [2, 6, 9], 
#      [3, 6, 9]]

# Output: 5

# Explanation:
# Sorting matrix elements gives us 
# {1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 

# Example 2:

# Input:
# R = 3, C = 1
# M = [[1], [2], [3]]
# Output: 2


import sys
class Solution:
    def median(self, matrix, r, c):
    	#code here 

        # doing this part because it is told that array is sorted row-wise only
    	low = sys.maxsize
    	high = -sys.maxsize
    	for i in matrix:
    	    low = min(low,i[0])
    	    high = max(high,i[-1])
    	
    	while(low <= high):
    	    
    	    m = low + (high - low)//2
    	    
    	    left = 0
    	    for i in matrix:
    	        left += self.howManyOnleft(i,c,m)
    	        
    	   # print(left,right,low,high,m)
    	    
    	    if(left <= ((r*c))/2):
    	        low = m + 1
    	    else:
    	        high = m - 1
    	       
        return low
	   
    def howManyOnleft(self,arr,n,target):
        l = 0
        h = n-1
        while(l <= h):
            mid = l + (h - l)//2
            if(arr[mid] <= target):
                l = mid + 1
            else:
                h = mid - 1
        return l