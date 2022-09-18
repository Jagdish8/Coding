# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

# Example 1:

# Input: 
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based
# indexing).

# Example 2:

# Input: 
# N = 2, M = 2
# Arr[][] = {{0, 0}, {1, 1}}
# Output: 1
# Explanation: Row 1 contains 2 1's (0-based
# indexing).


class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
        
        ans = -1
	    index = m - 1
	    
	    for i in range(n):
	        flag = False
	        while(index >= 0 and arr[i][index] == 1):
	            flag = True
	            index -= 1
            if(flag):
                ans = i
        
        if(ans == 0 and arr[0][-1] == 0):
            return -1
        return ans

# O(m+n)