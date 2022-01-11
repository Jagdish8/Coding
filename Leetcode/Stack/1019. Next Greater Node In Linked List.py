# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

# Example 1:


# Input: head = [2,1,5]
# Output: [5,5,0]
# Example 2:


# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
 

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if(not head):
            return []
        def reverse(root):
            if(not root or not root.next):
                return root
            last = reverse(root.next)
            root.next.next = root
            root.next = None
            return last
        head = reverse(head)
        ans = [0]
        st = [head.val]
        head = head.next
        while(head):
            while(st and st[-1] <= head.val):
                st.pop()
            if(st):
                ans.append(st[-1])
            else:
                ans.append(0)
            st.append(head.val)
            head = head.next
        return ans[::-1]