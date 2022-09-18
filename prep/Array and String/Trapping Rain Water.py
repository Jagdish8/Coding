# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        if(not height):
            return 0
        l = [0]*len(height)
        l[0] = height[0]
        for i in range(1,len(height)):
            l[i]=(max(height[i],l[i-1]))
        r = [0] * len(height)
        r[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            r[i]=(max(height[i],r[i+1]))
        s = []
        for i,j,k in zip(height,l,r):
            s.append(min(j,k) - i)
        return sum(s)

# stack
# notes



# two pointer

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
        # two pointers 
        # pointer i from the left
        # pointer j from the right
        while i <= j:
            # take the min height
            mi = min(height[i], height[j])
            # find the max min height
            mx = max(mx, mi)
            # the units of water being tapped is the diffence between max height and min height
            ans += mx - mi
            # move the pointer i if height[i] is smaller
            if height[i] < height[j]:
                i += 1
            # else move pointer j
            else:
                j -= 1
        return ans
