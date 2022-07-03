# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        
        if(N < M):
            return -1
         
        low = max(A)
        high = sum(A)
        res = -1
        
        while(low <= high):
            
            mid = low + (high-low)//2
            
            if(self.isValid(M,A,mid)):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
            
    def isValid(self,k,nums,target):
        m = 1
        s = 0
        
        for i in nums:
            s = s + i
            if(s > target):
                s = i
                m += 1
            if(m > k):
                return False
        
        return True
