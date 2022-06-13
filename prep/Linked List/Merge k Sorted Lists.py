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
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for l in lists:
            current = l
            while current:
                heap.append(current.val)
                current = current.next
        heapq.heapify(heap)
        merged_prehead = ListNode(-1)
        merged = merged_prehead
        while heap:
            val = heapq.heappop(heap)
            merged.next = ListNode(val)
            merged = merged.next
            
        return merged_prehead.next


# if use recursiove like merge 2 lists, gives tle
# or merge 2 lists and append, at last only one list will be left (TLE)

# using heap, complexity O(NlogK)
# N is the lenght of heap

# first go with recursive
# then this