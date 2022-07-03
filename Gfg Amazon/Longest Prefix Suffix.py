# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#



class Solution:
	def lps(self, s):

        n = len(s)
        
        # important
        if(s == s[::-1]):
            return n - 1

    
        if n == 0:
            return 0
            
        end_suffix = n-1
        end_prefix = n // 2 - 1

        while end_prefix >= 0:
            if s[end_prefix] != s[end_suffix]:
                if end_suffix != n-1:
                    end_suffix = n-1 
                else:
                    end_prefix -= 1
            else:
                end_suffix -= 1
                end_prefix -= 1
                
        return n-end_suffix-1


# Time Complexity: O(n)
# Auxiliary Space: O(1)
