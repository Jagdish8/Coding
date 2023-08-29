# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# https://leetcode.com/problems/longest-common-prefix/description/

import sys
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}
        smallest = sys.maxsize
        for each in strs:
            smallest = min(smallest, len(each))
            if(not each):
                return ""
            temp = trie
            for eachChar in each:
                if(eachChar not in temp):
                    temp[eachChar] = {}
                temp = temp[eachChar]
        ans = ""
        while(len(trie) == 1 and len(ans) < smallest):
            for each in trie:
                ans += each
            trie = trie[each]
        return ans
        