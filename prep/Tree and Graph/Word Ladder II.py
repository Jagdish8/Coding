# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 1000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.





class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if(endWord not in wordList):
            return []
        wordList = set(wordList)
        q = [[beginWord,[beginWord]]]
        ans = []
        flag = False
        while(q):
            seen = set()
            n = len(q)
            for i in range(n):
                popped = q.pop(0)
                node = popped[0]
                path = popped[1]
                if(node == endWord):
                    ans.append(path)
                    flag = True
                    continue
                for j in range(len(node)):
                    for k in range(26):
                        s = node[:j] + chr(97+k) + node[j+1:]
                        if(s in wordList):
                            seen.add(s)
                            q.append([s,path+[s]])
            if(flag):
                break
            wordList -= seen
        if(flag):
            return ans
        return []



# doing dfs causes TLE
# bfs is better


# if we want the path and ans in list[list] the outside vis cannot be used

# in the queue, first the node and then the path is added
# same like word ladder addition in the queue without the vis


# extra seen is used to not use the previous ones again
# after each level, seen is subtracted from the wordList

#flag is used, if for a level we got the answer, then no need to check for further level
# because it will be of more length than of the previous ans