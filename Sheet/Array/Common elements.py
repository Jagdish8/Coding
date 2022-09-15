https://practice.geeksforgeeks.org/problems/common-elements1132/1

Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

import sys
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        ans = []
        i = j = k = 0

        # for handling duplicate
        prev = sys.maxsize
        
        while(i < n1 and j < n2 and k < n3):
            
            if(A[i] == B[j] == C[k]):

                # duplicate check
                if(A[i] != prev):
                    prev = A[i]
                    ans.append(A[i])
                i += 1
                j += 1
                k += 1
            elif(A[i] < B[j]):
                i += 1
            elif(B[j] < C[k]):
                j += 1
            else:
                k += 1
        
        return ans