# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits):
            return []
        h = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        self.n = len(digits)
        self.an = []
        def solve(a,com):
            if(not a):
                self.an.append(com)
                return
            for i in h[a[0]]:
                solve(a[1:],com+i)
        solve(digits,"")
        return self.an
        
        