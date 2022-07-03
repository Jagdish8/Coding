# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#




class Solution:
	def minJumps(self, arr, n):
	    
	    if(not self.checkReachEnd(arr)):
	        return -1
	        
	    l = r = 0
	    res = 0
	    while(r < n-1):
	        far = 0
	        for i in range(l,r+1):
	            far = max(far,i+arr[i])
	        l = r + 1
	        r = far
	        res = res + 1
	    return res
	    
	def checkReachEnd(self,arr):
	    
	    lastPos = len(arr)-1
	    for i in range(len(arr)-2,-1,-1):
	        if(arr[i]+i >= lastPos):
	            lastPos = i
        if(lastPos == 0):
            return True
        return False