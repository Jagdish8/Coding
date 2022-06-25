# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reve(head):
            if(not head or not head.next):
                return head
            rest = reve(head.next)
            head.next.next = head
            head.next = None
            return rest
        
        if(not head.next):
            return head
        if(left == right):
            return head
        
        n = right - left + 1
        temp_left = left
        
        lala = head
        rev = head

        if(left != 1):
            while(left != 1):
                left -= 1
                lala = rev
                rev = rev.next
                
        # print(lala)
        # print(rev)


        temp = rev
        prev = rev
        while(n):
            prev = temp
            temp = temp.next
            n -= 1
            
        # print(prev)
        # print(temp)
        
        
        prev.next = None
        rev = reve(rev)
        # print(rev)
        
        an = rev
        while(an.next):
            an = an.next
        an.next = temp
        
        
        
        if(temp_left == 1):
            return rev

        lala.next = rev
        return head
        

# logic