# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
 

 class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if(not nums):
            return nums
        n = len(nums)
        nums = nums + nums
        left = [-1]
        st = [nums[-1]]
        for i in range((2*n)-2,-1,-1):
            while(st and nums[i] >= st[-1]):
                st.pop()
            if(st):
                left.append(st[-1])
            else:
                left.append(-1)
            st.append(nums[i])
        left = left[::-1]
        print(left)
        return left[:n]