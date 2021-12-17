# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def cal(l1,l2,c):
            if(not l1 and not l2 and not c):
                return None
            ans = 0
            if(l1):
                ans = ans + l1.val
                l1= l1.next
            if(l2):
                ans = ans + l2.val
                l2 = l2.next
            if(c):
                ans = ans + c
            if(ans >= 10):
                return ListNode(ans%10,next = cal(l1,l2,1))
            else:
                return ListNode(ans%10,next = cal(l1,l2,0))
        return cal(l1,l2,0)

# [2,4,3], l2 = [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
l3 = s.addTwoNumbers(l1,l2)
while(l3):
    print(l3.val)
    l3=l3.next
