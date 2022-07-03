# https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissionshttps://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions


import sys
class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
		
		low = 0
		high = n
		while(low <= high):
		    
		    cut1 = low + (high-low)//2
		    cut2 = n - cut1
		  #  print(cut1,cut2)
		    
		    l1 = -sys.maxsize if cut1 == 0 else ar1[cut1-1]
		    l2 = -sys.maxsize if cut2 == 0 else ar2[cut2-1]
		    r1 = sys.maxsize if cut1 == n else ar1[cut1]
		    r2 = sys.maxsize if cut2 == n else ar2[cut2]
		    
		    if(l1 <= r2 and r1 >= l2):
		        return max(l1,l2)+min(r1,r2)
		    
		    if(l1 > r2):
		        high = cut1 - 1
		    else:
		        low = cut1 + 1
	        