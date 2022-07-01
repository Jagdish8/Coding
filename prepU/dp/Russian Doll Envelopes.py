# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
 
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes = sorted(envelopes,key = lambda x : [x[0],-x[1]])
        # envelopes = sorted(envelopes)
        st = [envelopes[0]]
        
        print(envelopes)
        
        for i,j in enumerate(envelopes):
            if(st[-1][1] < j[1]):
                st.append(j)
            else:
                index = self.findPos(j,st)
                # print(j,index,st)
                st[index] = j
        return len(st)
                
    def findPos(self,val,arr):
        y = val[1]
        low = 0
        high = len(arr)-1
        while(low <= high):
            
            mid = low + (high-low)//2
            
            if(y <= arr[mid][1]):
                high = mid - 1
            else:
                low = mid + 1
        
        return low


# variation longest increasing subsequence
# same logic used

# why sorted by dec for second parameter:
# reason : https://leetcode.com/problems/russian-doll-envelopes/discuss/2071477/C%2B%2BJava-PythonBest-Explanation-with-Pictures
# to remove duplicate count

