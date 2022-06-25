# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            if(not head or not head.next):
                return head
            rest = rev(head.next)
            head.next.next = head
            head.next = None
            return rest
        def solve(l1,l2,carry):
            if(not l1 and not l2 and not carry):
                return None
            ans = 0
            if(l1):
                ans = ans + l1.val
                l1 = l1.next
            if(l2):
                ans = ans + l2.val
                l2 = l2.next
            if(carry):
                ans = ans + carry
            if(ans>9):
                ans = ans % 10
                carry = 1
            else:
                carry = 0
            return ListNode(ans,solve(l1,l2,carry))
        l1,l2 = rev(l1),rev(l2)
        return rev(solve(l1,l2,0))