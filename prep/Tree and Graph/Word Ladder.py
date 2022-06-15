# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if(endWord not in wordList):
            return 0
        wordList = set(wordList)
        q = [beginWord]
        ans = 0
        vis = set()
        vis.add(beginWord)
        while(q):
            print(q)
            ans = ans + 1
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if(node == endWord):
                    return ans
                
                for j in range(len(node)):
                    for k in range(26):
                        s = node[:j] + chr(97+k) + node[j+1:]
                        # print(s)
                        if(s in wordList and s not in vis):
                            # print(s)
                            vis.add(s)
                            q.append(s)   
        return 0

# first of wordList = set(wordList) is importan because search is O(1) but in list its O(n)

# use vis = set(), again faster instead of vis = [False .......]

# Idea is we have nodes, we need to find the shortest distance between source and destination

# DFS gives TLE, better to use BFS 

# nodes are connected in such a way that only one char differs from the nodes if they're connected


# firstly we add the source in the queue
# then use bfs technique  while(q) .........

# then for all in the queue , add the possible connected nodes

# now for finding the possible connected nodes for each node in queue, 
    # for each char in the node
    # change the first place char from all "abcde.....z" and check whether new string formed is in
    # wordlist and is not vis
    # eg:  node:  aed
    # possible nodes : aed,bed,ced,ded,...........
    # similarly for second place now
    # eg: node: aed
    #possible nodes : aad,abd,acd,.........
# In this way we'll add all the nodes which are not in vis and are present in wordList in the queue

# remaining is bfs