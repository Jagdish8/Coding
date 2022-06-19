# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"


from http.client import OK


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.trie = {}
        # self.m = sys.maxsize
        # self.w = ""
        # def findmin(t,s):
        #     for i in t:
        #         if("-" in i):
        #             if(len(s) < self.m):
        #                 self.w = s
        #                 self.m = len(s)
        #                 return
        #         findmin(t[i],s+"i")
        def replace(word):
            t = self.trie
            s = ""
            if(word[0] not in t):
                return word
            for i in word:
                if("-" in t):
                    # s += i
                    return s
                if(i in t):
                    s += i
                    t = t[i]
                else:
                    break
            if("-" in t):
                return s
            return word
        def trie(d):
            t = self.trie
            for i in d:
                if(i not in t):
                    t[i] = {}
                t = t[i]
            t["-"] = True
        for i in dictionary:
            trie(i)
        l = sentence.split(" ")
        print(l)
        print(self.trie)
        for i,j in enumerate(l):
            l[i] = replace(j)
        return " ".join(l)
        

# OK