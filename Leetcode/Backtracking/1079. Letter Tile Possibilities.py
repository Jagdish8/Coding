# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1

class Solution:
    def numTilePossibilities(self, tiles):
        res=set()
        def helper(t,curr,k):
            print(t,curr,k)
            if k==len(curr):
                res.add(curr)
                return
            for i in range(len(t)):
                helper(t[:i]+t[i+1:], curr+t[i], k)
        for i in range(1,len(tiles)+1):
            helper(tiles,'',i)
        return((len(res)))    