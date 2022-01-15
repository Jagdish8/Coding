# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# Example 2:

# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
# Example 3:

# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.
 

class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        n = len(arr)
        nge = [1]*n
        pge = [1]*n
        nse = [1]*n
        pse = [1]*n
        
        st = []
        for i in range(n):
            while len(st) and arr[st[-1]] > arr[i]:
                nse[i] = nse[i] + nse[st[-1]]
                st.pop()   
            st.append(i)
            
        st = []
        for i in range(n-1,-1,-1):
            while len(st) and arr[st[-1]] >= arr[i]:
                pse[i] = pse[i] + pse[st[-1]]
                st.pop()
            st.append(i)
            
        st = []
        for i in range(n):
            while len(st) and arr[st[-1]] < arr[i]:
                nge[i] = nge[i] + nge[st[-1]]
                st.pop()   
            st.append(i)
            
        st = []
        for i in range(n-1,-1,-1): 
            while len(st) and arr[st[-1]] <= arr[i]:
                pge[i] = pge[i] + pge[st[-1]]
                st.pop()
            st.append(i)
        sl = sum([a*b*c for a,b,c in zip(arr,pse,nse)])
        gr = sum([a*b*c for a,b,c in zip(arr,pge,nge)])
        print(gr,sl)
        return gr-sl