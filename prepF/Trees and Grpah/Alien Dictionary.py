# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".



from cmath import e
from distutils.fancy_getopt import wrap_text
from opcode import HAVE_ARGUMENT


# problem: 
#     we need to find the order of the letters 

#     eg: [wrt   0
#          wrf   1
#          er    2
#          ett   3
#          rftt  4]

#     it is given that the words are sorted lexicographically
#     meaning, wrt is lesser than wrf that means f comes after t in the dictionary

#     so we have
#     t -> f

#     wrf and er 
#     w comes before e
#     w -> e

#     similarly, r -> t and e -> r

#     so have w->e->r->t->f

#     o/p -> wertf


#     so basically they're asking the topoglogical sort if cycle is not there, is cycle is there return ""

# edge case: words: [abc,ab]
# input is wrong since ab should come before abc
# so return ""

# same way as course schedule 2

# add the remaining letters at last if they have no list in adjacency list



class Solution:
	def alienOrder(self, words: List[str]) -> str:

		al = {}

		if(len(set(words)) == 1):
			return "".join(set(words[0]))

# kept this adjacency list generation just to know that it is reducdant to check all words
# with each other since it is told that array is sorted

#         for i in range(len(words)-1):
#             for j in range(i+1,len(words)):

#                 index = 0
#                 a = ""
#                 b = ""
#                 while(index < min(len(words[i]),len(words[j]))):
#                     # print(words[i][index],words[j][index])
#                     if(words[i][index] != words[j][index]):
#                         a = words[i][index]
#                         b = words[j][index]
#                         break
#                     index += 1
#                 if(a and b):
#                     if(a not in al):
#                         al[a] = []
#                     if(b not in al[a]):
#                         al[a].append(b)


		for i,j in zip(words,words[1:]):
			index = 0
			a = ""
			b = ""
			minlength = min(len(i),len(j))
			
			# this test case should not be there, if it is told that array is sorted (["abc","ab"])
			if(i[:minlength] == j[:minlength] and len(j) == minlength and len(i) !=len(j)):
				return ""
				
			while(index < minlength):
				if(i[index] != j[index]):
					a = i[index]
					b = j[index]
					break
				index += 1
			if(a and b):
				if(a not in al):
					al[a] = []
				if(b not in al[a]):
					al[a].append(b)
		
		# to add this at last/start (doesn't matter) of path
		all_chars = set(''.join(words))
		missed_chars = all_chars - set(al)
		for ch in missed_chars:
			al[ch] = []    
		print(al)


		vis = set()
		dfs_vis = set()
		self.flag = True
		path = []

		def solve(node):

			if(not self.flag):
				return

			vis.add(node)
			dfs_vis.add(node)

			if(node in al):
				for i in al[node]:
					
					# if True for both cycle is there
					if(i in vis and i in dfs_vis):
						self.flag = False
						return
					if(i not in vis):
						solve(i)

			dfs_vis.remove(node)
			path.append(node)

		for i in al:
			if(i not in vis):
				solve(i)

		if(not self.flag):
			return ""
		return "".join(path[::-1])