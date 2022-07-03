# https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#

# https://www.youtube.com/watch?v=LkrsdWa69_Q

def kthSmallest(mat, n, k): 
    
    start = mat[0][0]
    end = mat[-1][-1]
    
    while(start <= end):
        
        midVal = start + (end-start)//2
        
        no_of_elements = 0
        for i in mat:
            no_of_elements += find(i,midVal)
        if(no_of_elements < k):
            start = midVal + 1
        else:
            end = midVal - 1
        
    return start
    
def find(arr,target):
    
    l = 0
    h = len(arr)-1
    while(l <= h):
        mid = l + (h - l)//2
        if(arr[mid] <= target):
            l = mid + 1
        else:
            h = mid - 1
    return l