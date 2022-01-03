# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if(len(nums)<3):
            return False
        st = [nums[-1]]
        min_stack = [nums[0]]
        for i in range(1,len(nums)):
            min_stack.append(min(min_stack[i-1],nums[i]))
        for j in range(len(nums)-2,-1,-1):
            while(st and st[-1] <= min_stack[j]):
                st.pop()
            if(st and st[-1]<nums[j]):
                return True
            st.append(nums[j])
        return False