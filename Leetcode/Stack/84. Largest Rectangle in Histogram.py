# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
            m = max(m,i*(k+j-1))
        return m
                
        