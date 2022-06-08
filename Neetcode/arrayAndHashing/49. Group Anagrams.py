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