# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if(not head or not head.next):
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        count = count // 2
        temp = head
        prev = head
        while(count):
            count -= 1
            prev = temp
            temp = temp.next
        prev.next = None
        last = reverse(temp)
        while(head):
            if(head.val == last.val):
                head = head.next
                last = last.next
            else:
                return False
        return True


# reverse second half and compare
# line 53 imp, to free up space 
        