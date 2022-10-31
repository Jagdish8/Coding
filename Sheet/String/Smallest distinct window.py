# https://practice.geeksforgeeks.org/problems/smallest-distant-window3132/1

# Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
# For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca.

 

# Example 1:

# Input : "AABBBCBBAC"
# Output : 3
# Explanation : Sub-string -> "BAC"
# Example 2:
# Input : "aaab"
# Output : 2
# Explanation : Sub-string -> "ab"


class Solution:
    def findSubString(self, str):
        # Your code goes here
        count = len(set(str))
        i =j = 0
        h = {}
        ans = len(str)
        while(j<len(str)):
            if(str[j] not in h):
                h[str[j]] = 0
            h[str[j]] += 1
            if(len(h) < count):
                j += 1
            else:
                # ans = min(j-i+1,ans)
                # print(h,ans,i,j)
                while(len(h) == count):
                    h[str[i]] -= 1
                    if(h[str[i]] == 0):
                        del h[str[i]]
                    i += 1
                ans = min(j - i + 1,ans)
                j += 1
        if(ans == len(str)):
            return len(str)
        return ans + 1
    