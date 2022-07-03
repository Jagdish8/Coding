# https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		v = [0]*26
		ans = ""
		st = []
		
		for j in A:
            v[ord(j)-ord("a")] += 1
            st.append(j)
            while(st and v[ord(st[0])-ord("a")] > 1):
                st.pop(0)
            if(st):
                ans += st[0]
            else:
                ans += "#"
        
        return ans