# Given a character array s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

# Your code must solve the problem in-place, i.e. without allocating extra space.

 

# Example 1:

# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Example 2:

# Input: s = ["a"]
# Output: ["a"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
# There is at least one word in s.
# s does not contain leading or trailing spaces.
# All the words in s are guaranteed to be separated by a single space.


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while(i < j):
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        i = 0
        n = len(s)
        st = ""
        start = 0
        # print(s)
        while(i < n):
            # print(s)
            if(s[i] == " "):
                st = st[::-1]
                j = 0
                while(start < i):
                    s[start] = st[j]
                    j += 1
                    start += 1
                st = ""
                start = i+1
                i += 1
            else:
                st += s[i]
                i += 1
        st = st[::-1]
            # print(st,start,i)
        j = 0
        while(start < i):
            s[start] = st[j]
            j += 1
            start += 1

# brain