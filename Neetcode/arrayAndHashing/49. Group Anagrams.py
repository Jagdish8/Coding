https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if(not strs):
        #     return [[""]]
        ans = []
        h = {}
        for i in strs:
            s = ""
            for j in i:
                s+=j
            if(str(sorted(s)) in h):
                h[str(sorted(s))].append(s)
            else:
                h[str(sorted(s))] = [s]
        for i in h.values():
            ans.append(i)
        return ans
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#       Input: strs = ["eat","tea","tan","ate","nat","bat"]
#       Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        h = {}
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1
            s = tuple(count)
            if(s not in h):
                h[s] = [i]
            else:
                h[s].append(i)
        return h.values()
    
    
