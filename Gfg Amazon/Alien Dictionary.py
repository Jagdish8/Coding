# https://practice.geeksforgeeks.org/problems/alien-dictionary/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    def findOrder(self,dict, N, K):
        
        al = {}
        
		for i,j in zip(dict,dict[1:]):
			index = 0
			a = ""
			b = ""
			minlength = min(len(i),len(j))
			
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
        
        all_words = set("".join(dict))
        all_words_in_al = set("".join(al.keys()))
        missed = all_words - all_words_in_al
        for i in missed:
            al[i] = []
            
        self.path = ""
        vis = set()
        dfs_vis = set()
        self.flag = False
        # print(al)
        
        def solve(node):
            
            if(self.flag):
                return
            
            vis.add(node)
            dfs_vis.add(node)
            for i in al[node]:
                if(i in vis and i in dfs_vis):
                    self.flag = True
                    return
                if(i not in vis):
                    solve(i)
                    
            dfs_vis.remove(node)
            self.path += node
        
        for i in al:
            if(i not in vis):
                solve(i)
        
        if(self.flag):
            return ""
        # print(self.path[::-1])
        return self.path[::-1]