# https://leetcode.com/problems/palindrome-pairs/

# https://leetcode.com/problems/palindrome-pairs/solution/
# approach 3

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        trie = {}
        ans = []
        
        #classic trie generation with adding the pal list containing index of the word if rest part of the word is pal or not from that specific char
        # reason for adding pal is on line 46
        for i,word in enumerate(words):
            word = word[::-1]
            temp = trie
            for j,c in enumerate(word):
                
                # checking for pal or not from that specific char
                if(word[j:] == word[j:][::-1]):
                    if("pal" not in temp):
                        temp["pal"] = []
                    temp["pal"].append(i)
                if(c not in temp):
                    temp[c] = {}
                temp = temp[c]
            temp[None] = i
            
        for i,word in enumerate(words):
            temp = trie
            for j,c in enumerate(word):
                
                # checking for 1 st word is longer than the second word
                if(None in temp):
                    if(word[j:] == word[j:][::-1]):
                        ans.append([i,temp[None]])
                if(c not in temp):
                    break
                temp = temp[c]
                
            # else is executed only if whole for loop is executed without break occuring
            # this else part is for first word is equals to smaller lenght than the seconf word
            else:
                if(None in temp and i != temp[None]):
                    ans.append([i,temp[None]])
                # now for checking whether the rest part is pal or not we have iterate again and again, thats why while generating the trie we can take care of that.
                if("pal" in temp):
                    for j in temp["pal"]:
                        ans.append([i,j])
        
        return ans
                
                
