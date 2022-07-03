# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#



class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        h = {0:1}
        prefix_sum = 0
        count = 0
        for i in range(n):
            prefix_sum += arr[i]
            if(prefix_sum - 0 in h):
                count = count + h[prefix_sum - 0]
            if(prefix_sum not in h):
                h[prefix_sum] = 0
            h[prefix_sum] += 1
        return count