# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#iterative
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not list1 and not list2):
            return list1
        if(not list1):
            return list2
        if(not list2):
            return list1
        
        def add(l1,l2):
            head = l1
            prev = None
            while(l1 and l2):
                if(l1.val <= l2.val):
                    prev = l1
                    l1 = l1.next
                else:
                    temp = l2.next
                    prev.next = l2
                    l2.next = l1
                    prev = l2
                    l2 = temp
            if(l2):
                prev.next = l2
            return head
        if(list1.val <= list2.val):
            return add(list1,list2)
        return add(list2,list1)

# recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not list1 and not list2):
            return list1
        if(not list1):
            return list2
        if(not list2):
            return list1
        
        def add(l1,l2):
            if(not l1):
                return l2
            if(not l2):
                return l1
            if(l1.val <= l2.val):
                l1.next = add(l1.next,l2)
                return l1
            else:
                l2.next = add(l1,l2.next)
                return l2
        if(list1.val <= list2.val):
            return add(list1,list2)
        return add(list2,list1)