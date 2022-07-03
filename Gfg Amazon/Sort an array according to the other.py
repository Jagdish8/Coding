# https://practice.geeksforgeeks.org/problems/relative-sorting4323/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here

        A1 = sorted(A1)
        h = {}
        temp = []
        for i in A2:
            if(i not in h):
                h[i] = True
                first = self.find(A1,i,True)
                if(first == -1):
                    continue
                second = self.find(A1,i,False)
                temp = temp + A1[first:second+1]
                A1 = A1[:first] + A1[second+1:]

        return temp + A1
        
    def find(self,nums,target,flag):
        
        low = 0
        high = len(nums)-1
        res = -1
        
        while(low <= high):
            
            mid = low + (high - low)//2
            if(target == nums[mid]):
                res = mid
                if(flag):
                    high = mid - 1
                else:
                    low = mid + 1
            elif(target > nums[mid]):
                low = mid + 1
            else:
                high = mid - 1
                
        return res
        