# # https://leetcode.com/problems/maximum-number-of-balloons/description/

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = {}
        for i in text:
            if(i not in h):
                h[i] = 0
            h[i] += 1
        ans = sys.maxsize
        for i in "ol":
            if(i in h):
                h[i] //= 2
            else:
                return 0
        for i in "balon":
            if(i not in h):
                return 0
            ans = min(ans, h[i])
        return ans