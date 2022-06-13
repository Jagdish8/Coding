# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#       Input: strs = ["eat","tea","tan","ate","nat","bat"]
#       Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        h = {}
        ans = []
        for i in strs:
            s = str(sorted(i))
            if(s not in h):
                h[s] = [i]
            else:
                h[s].append(i)
        for i in h:
            ans.append(h[i])
        return ans

# using simple hashmap functionality

        