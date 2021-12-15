# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(not head):
            return head
        while(head and head.val == val):
            head=head.next
        if(not head):
            return head
        def cal(head,val):
            if(not head):
                return None
            while(head and head.val == val):
                head = head.next
            if(not head):
                return None
            head.next = cal(head.next,val)
            return head
        head.next = cal(head.next,val)
        return head