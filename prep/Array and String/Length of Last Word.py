https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)-1
        start = n
        
        while(start >= 0 and s[start] == " "):
            start -= 1
            
        if(start == -1):
            return 0
        
        end = start
        
        while(end >= 0 and s[end] != " "):
            end -= 1
            
        return start - end
        