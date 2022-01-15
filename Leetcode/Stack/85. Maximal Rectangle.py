# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

 class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            n = len(heights)
            l = [1]*n
            r = [1]*n
            st = []
            for i in range(n):
                while(st and heights[st[-1]] >= heights[i] ):
                    l[i] = l[i] + l[st.pop()]
                st.append(i)
            st = []
            for i in range(n-1,-1,-1):
                while(st and heights[st[-1]] > heights[i] ):
                    r[i] = r[i] + r[st.pop()]
                st.append(i)
            m = 0
            for i,j,k in zip(heights,l,r):
                if(i > 0):
                    m = max(m,i*(k+j-1))
            return m
        l = []
        for i in matrix[0]:
            l.append(int(i))
        m = largestRectangleArea(l)
        for i in range(1,len(matrix)):
            l1 = [int(i) for i in matrix[i]]
            for j in range(len(l1)):
                if(l[j] > 0 and l1[j] > 0):
                    l1[j] = l1[j] + l [j]
            m = max(largestRectangleArea(l1),m)
            l = l1
        return m
        
        