# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # Input: s = "ababcbacadefegdehijhklij"
        # Output: [9,7,8]
        # Explanation:
        # The partition is "ababcbaca", "defegde", "hijhklij".
        # This is a partition so that each letter appears in at most one part.
        # A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
        
        ans = []
        h = {}
        m = -1
        for i,j in enumerate(s):
            h[j] = i
        print(h)
        for i,j in enumerate(s):
            m = max(m,h[j])
            if(h[j] == i and m == h[j]):
                if(ans):
                    ans.append(i-sum(ans)+1)
                else:
                    ans.append(i+1)
        return ans

# simple approach using hash map
# hashmap stores the last index of a perticular element

# dry run
# s = "ababcbacadefegdehijhklij"
# ans = []
# h = {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
# m = -1

# i = 0
# j = a
# m = max(m,h[j]) = 8
# 0 != 8

# i = 1
# j = b
# m = max(8,6) = 8
# 1 != 8

# till i = 8 there are no elements which are have h[element] > m

# ok
