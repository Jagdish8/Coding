https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1

# Given an array arr of n positive integers and a number k.
#  One can apply a swap operation on the array any number of times, i.e
#   choose any two index i and j (i < j) and swap arr[i] , arr[j] .
#    Find the minimum number of swaps required to bring all the numbers less than
#     or equal to k together, i.e. make them a contiguous subarray.

# Example 1:

# Input : 
# arr[ ] = {2, 1, 5, 6, 3} 
# K = 3
# Output : 
# 1
# Explanation:
# To bring elements 2, 1, 3 together,
# swap index 2 with 4 (0-based indexing),
# i.e. element arr[2] = 5 with arr[4] = 3
# such that final array will be- 
# arr[] = {2, 1, 3, 6, 5}

# Example 2:

# Input : 
# arr[ ] = {2, 7, 9, 5, 8, 7, 4} 
# K = 6 
# Output :  
# 2 
# Explanation: 
# To bring elements 2, 5, 4 together, 
# swap index 0 with 2 (0-based indexing)
# and index 4 with 6 (0-based indexing)
# such that final array will be- 
# arr[] = {9, 7, 2, 5, 4, 7, 8}


import sys
def minSwap (arr, n, k) : 
    #Complete the function
    count = 0
    for i in arr:
        if(i <= k):
            count += 1
            
    if(count == 0 or count == 1 or count == n):
        return 0
    
    i = j = 0
    n = len(arr)
    ans = sys.maxsize
    temp_count = 0

    while(j < n):
        if(arr[j] <= k):
            temp_count += 1
        if(j - i + 1 < count):
            j += 1
        else:
            ans = min(ans,count - temp_count)
            if(arr[i] <= k):
                temp_count -= 1
            i += 1
            j += 1
            
    
    return ans


# A simple approach is to use two pointer technique and sliding window.

# Find count of all elements which are less than or equals to ‘k’.
#  Let’s say the count is ‘cnt’


# Using two pointer technique for window of length ‘cnt’,
#  each time keep track of how many elements in this range are greater than ‘k’.
#   Let’s say the total count is ‘bad’.


# Repeat step 2, for every window of length ‘cnt’ and take minimum of count ‘bad’ among them.
#  This will be the final answer