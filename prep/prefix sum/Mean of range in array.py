# https://practice.geeksforgeeks.org/problems/mean-of-range-in-array2123/1?page=1&category[]=prefix-sum&sortBy=submissions

import math
class Solution:  
    def findMean(self, arr, queries, n, q): 
        # Complete the function
        prefix = [arr[0]]
        for i in arr[1:]:
            prefix.append(prefix[-1]+i)
        # print(prefix)
            
        ans = []
        for i,j in zip(range(0,len(queries),2),range(1,len(queries),2)):
            # print(i,j)
            s = prefix[queries[j]]-prefix[queries[i]]+arr[queries[i]]
            c = queries[j]-queries[i]+1
            # print(s,c)
            ans.append(math.floor(s/c))
        return ans