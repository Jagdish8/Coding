# https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1

class Solution:
    def maxLen(self,arr, N):
        # code here
        hash_map = {}  
        curr_sum = 0 
        max_len = 0 
        # ending_index = -1 
    
        for i in range (0, n): 
            if(arr[i] == 0): 
                arr[i] = -1 
            else: 
                arr[i] = 1 
        for i in range (0, n): 
            curr_sum = curr_sum + arr[i] 
            if (curr_sum == 0): 
                max_len = i + 1 
                ending_index = i 
            if curr_sum in hash_map:
                if max_len < i - hash_map[curr_sum]:
                    max_len = i - hash_map[curr_sum]
                    # ending_index = i
            else: 
                hash_map[curr_sum] = i
            
        return max_len

# ending index can be used for returning the subarray 