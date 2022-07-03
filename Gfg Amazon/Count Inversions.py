# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:

    def __init__(self):
        self.ans = 0
        
    def inversionCount(self, arr, n):
        self.mergeSort(arr)
        return self.ans
        
    def mergeSort(self,arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    self.ans += len(L)-i
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
     
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
