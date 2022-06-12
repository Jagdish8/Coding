https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 0
        n = len(triplets)
        arr = []
        while(i<n):
            if(triplets[i][0]>target[0] or triplets[i][1]>target[1] or triplets[i][2]>target[2]):
                pass
            else:    
                arr.append(triplets[i])
            i += 1
        for i in range(len(arr)-1):
            arr[i+1] = [max(arr[i][0],arr[i+1][0]),max(arr[i][1],arr[i+1][1]),max(arr[i][2],arr[i+1][2])]
        if(not arr):
            return False
        if(arr[-1] == target):
            return True
        return False