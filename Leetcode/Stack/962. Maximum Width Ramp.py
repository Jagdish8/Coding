# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        for i in range(len(nums)):
            if (not st):
                st.append((nums[i],i))
            else:
                if(st[-1][0] > nums[i]):
                    st.append((nums[i],i))
        #print(st)
        m = -1
        for i in range(len(nums)-1,-1,-1):
            while(st and st[-1][0] <= nums[i]):
                m = max(m,i-st[-1][1])
                st.pop()
            if(not st):
                return m
        return m