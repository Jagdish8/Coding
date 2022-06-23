# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.


# approach:

# We have two pointers, use i to scan S, and use j to scan each word in words.

# The two letters currently pointed by the two pointers must be equal, otherwise the word is not stretchy, we return false.

# Firstly, for S and word, we can calculate the length of the susbtrings which contains the repeated letters of the letter currently pointed by the two pointers, and get len1 and len2.

# Then, if we find that len1 is smaller than 3, it means the letter cannot be extended, so len1 must equals to len2,otherwise this word is not stretchy. Othercase would be if len2>len1 return False

# Finally, if the word is stretchy, we need to guarantee that both of the two pointers has scanned the whole string.


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def solve(word):
            if(word == s):
                return True
            if(len(word) >= len(s)):
                return False
            i = j = 0
            while(i<len(s) and j<len(word)):
                if(s[i] != word[j]):
                    return False
                else:
                    len1 = getCount(s,i)
                    len2 = getCount(word,j)
                    if(len2 > len1 or (len1 < 3 and len1 != len2)):
                        return False
                    i += len1
                    j += len2
            return True if (i == len(s) and j == len(word)) else False
        def getCount(word,j):
            i = j
            while(j<len(word) and word[j] == word[i]):
                j += 1
            return j - i 
        count = 0
        for i in words:
            if(solve(i)):
                count += 1
        return count

