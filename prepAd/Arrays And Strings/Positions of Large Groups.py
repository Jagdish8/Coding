# In a string s of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in increasing order by start index.

 

# Example 1:

# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:

# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:

# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        h = {}
        ans = []
        i = j = 0
        
        while(j < len(s)):
            
            if(s[j] not in h):
                h[s[j]] = 0
            h[s[j]] += 1
            
            if(len(h) <= 1):
                j += 1
                if(j == len(s) and j-i+1 > 3):    # one of the edge case  eg: "aaa"
                    ans.append([i,j-1])
            else:
                if(j-i+1 > 3):
                    ans.append([i,j-1])
                while(len(h) != 1):
                    h[s[i]] -= 1
                    if(h[s[i]] == 0):
                        del h[s[i]]
                    i += 1
                j += 1
                
        return ans

# sliding window approach

# using no extra space:

#     def largeGroupPositions(self, S):
#         i, j, N = 0, 0, len(S)
#         res = []
#         while i < N:
#             while j < N and S[j] == S[i]:
#                 j += 1
#             if j - i >= 3:
#                 res.append([i, j - 1])
#             i = j
#         return res


