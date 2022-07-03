# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        
        m = 0
        h = set(arr)
            
        for i in arr:
            
            if(i-1 not in h):
                count = 0
                temp = i
                while(temp in h):
                    count += 1
                    temp += 1
                m = max(count,m)
        
        return m