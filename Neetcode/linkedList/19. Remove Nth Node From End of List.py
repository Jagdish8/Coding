https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head.next):
            return head.next
        l = 0
        temp = head
        while(temp):
            l += 1
            temp = temp.next
        n = l - n
        temp = head
        if(n == 0):
            return head.next
        while(n):
            if(n == 1):
                temp.next = temp.next.next
            n -= 1
            temp = temp.next
            # print(temp,n)
        return head
        