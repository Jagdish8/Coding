# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        c1 = c2 = 0
        while(a):
            c1 += 1
            a = a.next
        while(b):
            b = b.next
            c2 += 1
        if(c1 > c2):
            diff = c1 - c2
            while(diff):
                diff -= 1
                headA = headA.next
        else:
            diff = c2 - c1
            while(diff):
                diff -= 1
                headB = headB.next
        while(headA != headB):
            headA = headA.next
            headB = headB.next
        return headA
            
        