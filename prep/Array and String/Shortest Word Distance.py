    # https://leetcode.com/problems/shortest-word-distance/

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