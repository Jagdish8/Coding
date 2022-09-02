# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head):
            return None
        
        slow = head
        fast = head
        self.flag = False
        
        while(fast and fast.next):
            
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                self.flag = True
                break
        
        
        if(not self.flag):
            return None
        
        cur = head
        while(cur != slow):
            cur=cur.next
            slow=slow.next
        return cur