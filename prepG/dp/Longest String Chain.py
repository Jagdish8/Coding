# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

 

# Example 1:

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# Example 2:

# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# Example 3:

# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.



class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        # using hashtable O(NlogN)
        self.h  = {}
        for i in words:
            self.h[i] = 1
        words = sorted(words,key = len)
        
        for i,j in enumerate(words):
            
            for l in range(len(j)):
                new_word_after_delete = j[:l] + j[l+1:]
                if(new_word_after_delete in self.h):
                    self.h[j] = max(self.h[j],1+self.h[new_word_after_delete])
        
        print(self.h)
        return max(self.h.values())

    
        # using dp O(N**2)
            # words = sorted(words,key = len)
            # dp = [1 for i in words]
            # for i in range(1,len(words)):
            #     for j in range(i):
            #         word1 = words[i]
            #         word2 = words[j]
            #         if(len(word1)-len(word2) == 1):
            #             x = y = 0
            #             while(x<len(word1) and y< len(word2)):
            #                 if(word1[x] != word2[y]):
            #                     break
            #                 x += 1
            #                 y += 1
            #             if(word1[x+1:] == word2[y:]):
            #                 dp[i] = max(dp[i],dp[j]+1)
            # # print(dp)
            # return max(dp)
                        

# using dp:
# similar appraoch as longest increasing subsequence with some modifications

# using hashtable:
# start from start
# after deleting each element check whether element is present in map:
# if yes then get max
# video
# https://www.youtube.com/watch?v=pXG3uE_KqZM