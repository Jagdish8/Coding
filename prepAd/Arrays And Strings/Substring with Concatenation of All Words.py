# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
 


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        h = {}
        for i in words:
            if(i not in h):
                h[i] = 0
            h[i] += 1
        
        wordLen = len(words[0])
        totalLen = len(words) * wordLen
        n = len(s)
        
        ans = []
        
        for left in range(n - totalLen + 1):
            seen = {}
            
            for right in range(len(words)):
                startIndex = left + right*wordLen
                temp_word = s[startIndex : startIndex + wordLen]
                if(temp_word not in h):
                    break
                if(temp_word not in seen):
                    seen[temp_word] = 0
                seen[temp_word] += 1
                if(seen[temp_word] > h[temp_word]):
                    break
                    
            if(seen == h):
                ans.append(left)
        
        return ans
                
                
        

# video : https://www.youtube.com/watch?v=06Ym9c7SuOU
# sliding window approach