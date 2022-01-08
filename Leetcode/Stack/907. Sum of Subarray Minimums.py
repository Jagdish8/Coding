# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def solve(start,end,a,idx):
            st = []
            ans = [1 for i in range(start,end,idx)]
            for i in range(start,end,idx):
                while(st and a[st[-1]] > a[i]):
                    ans[i] = ans[i] + ans[st[-1]]
                    st.pop()
                st.append(i)
            return ans
        def solve1(start,end,a,idx):
            st = []
            ans = [1 for i in range(start,end,idx)]
            for i in range(start,end,idx):
                while(st and a[st[-1]] >= a[i]):
                    ans[i] = ans[i] + ans[st[-1]]
                    st.pop()
                st.append(i)
            return ans
        left = solve(0,len(arr),arr,+1)
        print(left)
        right = solve1(len(arr)-1,-1,arr,-1)
        print(right)
        return sum([l*r*i for l,r,i in zip(left,right,arr)]) % (10 ** 9 + 7)