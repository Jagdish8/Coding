# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
# Example 3:

# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        n = len(s)
        def solve(index,current,vis):
            nonlocal ans,n
            if(index == n):
                ans = max(ans,current)
                return
            for i in range(index,n):
                # print(s[index:i])
                if(s[index:i+1] not in vis):
                    solve(i+1,current+1,vis+(s[index:i+1],))
        solve(0,0,())
        return ans