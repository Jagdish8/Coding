# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        odd = head
        even = head.next
        even_head = head.next
        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
            
        