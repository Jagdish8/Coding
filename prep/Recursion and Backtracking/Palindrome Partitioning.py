# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.ans = []
        def ispal(pal):
            if(not pal):
                return False
            if(pal==pal[::-1]):
                return True
            return False
        
        def solve(s,com):
            
            if(not s):
                self.ans.append(com[:])
                return
            
            for i in range(len(s)):
                if(ispal(s[:i+1])):
                    solve(s[i+1:],com+[s[:i+1]])
            
        solve(s,[])
        return self.ans

        