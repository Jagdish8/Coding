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



#using recursion
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def cal(m,n,c):
            if(not m and not n and not c):
                return None
            ans = 0
            if(c):
                ans = ans + c
            if(m):
                ans = ans + m.val
                m = m.next
            if(n):
                ans = ans + n.val
                n = n.next
            if(ans>9):
                return ListNode(ans%10,cal(m,n,1))
            else:
                return ListNode(ans,cal(m,n,0))
        def rev(head):
            if(not head or not head.next):
                return head
            last = rev(head.next)
            head.next.next = head
            head.next = None
            return last
        m = rev(l1)
        n = rev(l2)
        return rev(cal(m,n,0))
        
# using stack
    # using 2 stacks