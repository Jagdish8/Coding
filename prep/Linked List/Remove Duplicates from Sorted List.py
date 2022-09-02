# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head):
            return head
        t1 = head
        t2 = head.next
        while(t2):
            while(t2 and t1.val == t2.val):
                t2 = t2.next
            if(t2):
                t1.next = t2
                t1 = t1.next
                t2 = t1.next
            else:
                t1.next = None
                return head
        return head
        