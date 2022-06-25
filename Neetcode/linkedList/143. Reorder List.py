# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        def reverse(head):
            if(not head or not head.next):
                return head
            rest = reverse(head.next)
            head.next.next = head
            head.next = None
            return rest
        c = 0
        
        while(temp):
            c += 1
            temp = temp.next
        c =c // 2 
        
        temp = head
        while(c):
            temp = temp.next
            c -= 1
        
        rev = temp.next
        temp.next = None
        rev = reverse(rev)
        
        # print(head)
        # print(rev)
        
        temp = head
        while(rev):
            k = temp.next
            temp.next = rev
            k1 = rev.next
            rev.next = k
            rev = k1
            temp = k
            
        # print(temp.next)
        
        return head
    
    