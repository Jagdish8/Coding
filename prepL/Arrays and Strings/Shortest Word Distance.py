# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1


# intuition
# with extra space 
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        h = {}
        m = sys.maxsize
        for i,j in enumerate(wordsDict):
            if(j == word1 or j == word2):
                if(j not in h):
                    h[j] = []
                h[j].append(i)
        for i in h[word1]:
            for j in h[word2]:
                m = min(m,abs(i-j))
                if(m == 1):
                    return 1
        return m


# without using extra space
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        i1 = -1
        i2 = -1
        m = sys.maxsize
        
        for i,j in enumerate(wordsDict):
            if(j == word1):
                i1 = i
            elif(j == word2):
                i2 = i
            if(i1 != -1 and i2 != -1):
                m = min(m,abs(i1-i2))
                if(m == 1):
                    return 1
        return m