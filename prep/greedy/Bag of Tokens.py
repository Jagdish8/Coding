# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
#         Explanation
#         Sort tokens.
#         Buy at the cheapest and sell at the most expensive.


#         Complexity
#         Time O(sort)
#         Space O(sort)
        
        tokens = sorted(tokens)
        i = 0
        j = len(tokens)-1
        score = 0
        while( i <= j ):
            if( tokens[i] <= power):
                score += 1
                power -= tokens[i]
                i += 1
            elif ( score >= 1 and i < j):
                score -= 1
                power += tokens[j]
                j -= 1
            else: 
                break
        return score;