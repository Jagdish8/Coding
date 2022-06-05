https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1):
            return list2
        if(not list2):
            return list1
        temp1 = list1
        temp2 = list2
        root = ListNode(0)
        ans = root
        while(temp1 and temp2):
            if(temp1.val > temp2.val):
                ans.next = ListNode(temp2.val)
                temp2 = temp2.next
            else:
                ans.next = ListNode(temp1.val)
                temp1 = temp1.next
            ans = ans.next
            # print(root)
        if(temp1):
            ans.next = temp1
        if(temp2):
            ans.next = temp2
        return root.next