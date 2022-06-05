https://leetcode.com/problems/reorder-list/

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
        self.l = 0
        temp = head
        while(temp):
            self.l += 1
            temp = temp.next
        if(self.l == 1 or self.l == 2):
            return head
        def rev(head):
            if(not head or not head.next):
                return head
            self.l -= 1
            ans = rev(head.next)
            head.next.next = head
            head.next = None
            return ans
        self.l = 1 + self.l // 2 
        temp = head
        while(self.l):
            self.l -= 1
            temp = temp.next
        r = rev(temp)
        temp = head
        # print(head)
        # print(r)
        while(r):
            a = temp.next
            temp.next = ListNode(r.val)
            r = r.next
            temp.next.next = a
            temp = a
        temp = head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
        return head
    