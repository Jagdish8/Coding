# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head):
            return head
        
        cur = head
        prev = None
        
        while(cur and cur.next):
            if(cur.val != cur.next.val):
                prev = cur
                cur = cur.next
            else:
                while(cur.next and cur.val == cur.next.val):
                    cur = cur.next
                # if(prev):
                #     prev.next = cur.next
                # else:
                #     prev = cur.next
                #     head = cur.next
                # cur = cur.next
                
                if( not prev):
                    head=cur.next
                else:
                    prev.next=cur.next
                cur=cur.next
        return head