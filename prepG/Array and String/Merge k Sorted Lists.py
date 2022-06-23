# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


from heapq import heapify,heappush,heappop

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        heapify(heap)
        
        for l in lists:
            if(l):
                heappush(heap,(l.val,id(l),l))
                
        merged_prehead = ListNode(-1)
        merged = merged_prehead
        
        while heap:
            
            val,i,node = heappop(heap)
            merged.next = ListNode(val)
            merged = merged.next
            if(node.next):
                heappush(heap,(node.next.val,id(node.next),node.next))
                
        return merged_prehead.next

# first store heads of all the linked lists and then inside while do the operations

# O(Nlogk) K - size of lists

# O(n) + O(k) n - no. of total nodes