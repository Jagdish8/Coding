# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr = sorted(arr)
        dep = sorted(dep)
        res = 0
        plat = 0
        i = j = 0
        while(i < n and j < n):
            if(arr[i] <= dep[j]):
                plat += 1
                res = max(plat,res)
                i += 1
            else:
                plat -= 1
                j += 1
        return res