# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#



class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        
        st = [(a[0],0)]
        ans = [1]
        
        for i in range(1,n):
            while(st and st[-1][0] <= a[i]):
                st.pop()
            if(st):
                ans.append(i - st[-1][1])
            else:
                ans.append(i + 1)
            st.append((a[i],i))
            
        return ans