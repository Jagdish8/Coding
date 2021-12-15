# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=""
        temp = head
        while(temp):
            s+=str(temp.val)
            temp = temp.next
        def reverse(head):
            if(not head or not head.next):
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next=None
            return last
        rev = reverse(head)
        temp = rev
        while(temp):
            if(str(temp.val) != s[0]):
                return False
            temp = temp.next
            s=s[1:]
        return True