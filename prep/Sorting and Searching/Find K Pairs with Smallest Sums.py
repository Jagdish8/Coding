# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        h = []
        heapify(h)
        
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                total = nums1[i] + nums2[j]
                if(len(h)<k):
                    heappush(h,[-total,nums1[i],nums2[j]])
                else:
                    if(total > -h[0][0]):
                        break
                    heappush(h,[-total,nums1[i],nums2[j]])
                    heappop(h)
        
        return [[i,j] for _,i,j in h]