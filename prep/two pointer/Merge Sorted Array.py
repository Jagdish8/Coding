# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(not nums1):
            nums1 = nums2
            return
        i = 0
        j = 0
        c = -1
        while(i<m and j<n):
            if(nums1[m-i-1] < nums2[n-j-1]):
                nums1[c] = nums2[n-j-1]
                j += 1
            else:
                nums1[c] = nums1[m-i-1]
                i += 1
            c -= 1
        i=0
        while(j != n):
            nums1[i] = nums2[i]
            j += 1
            i += 1