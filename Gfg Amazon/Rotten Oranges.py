# https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


	def orangesRotting(self, grid):
		#Code here
		q = []
		self.r = len(grid)
		self.c = len(grid[0])
		
		for i in range(self.r):
		    for j in range(self.c):
		        if(grid[i][j] == 2):
		            q.append([i,j])
	    time = 0
	    if(not q):
	        return time
	    while(q):
	        time += 1
	        temp = []
	        for i,j in q:
	            if(i+1 < self.r and grid[i+1][j] == 1) :
	                temp.append([i+1,j])
	                grid[i+1][j] = 2
	            if(i-1 > -1 and grid[i-1][j] == 1):
	                temp.append([i-1,j])
	                grid[i-1][j] = 2
                if(j+1 < self.c and grid[i][j+1] == 1):
	                temp.append([i,j+1])
	                grid[i][j+1] = 2
                if(j-1 > -1 and grid[i][j-1] == 1):
	                temp.append([i,j-1])
	                grid[i][j-1] = 2
	        q = temp
        for i in grid:
            for j in i:
                if(j == 1):
                    return -1
        return time - 1