# https://practice.geeksforgeeks.org/problems/three-way-partitioning/1

# Given an array of size n and a range [a, b].
#  The task is to partition the array around the range such that array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order.
#  You are required to return the modified array.

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    
	    index = 0
	    i = 0
	    j = n - 1
	    
	    while(i <= j):
	        if(array[i] < a):
	            array[i],array[index] = array[index],array[i]
	            index += 1
	            i += 1
            elif(array[i] > b):
                array[j],array[i] = array[i],array[j]
                j -= 1
            else:
                i += 1
        
        return array