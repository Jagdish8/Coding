# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = ""
        m = sys.maxsize
        for i in strs:
            m = min(len(i),m)
        if(m == 0):
            return pre
        i = 0
        while(i < m):
            for j in range(1,len(strs)):
                if(strs[j-1][i] == strs[j][i]):
                    continue
                else:
                    return pre
            pre += strs[-1][i]
            i += 1
        return pre

# brain