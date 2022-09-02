# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # O(N),O(N)
        # if(not root):
        #     return None
        # st = [root]
        # while(st):
        #     q = []
        #     i = 0
        #     while(i < len(st)-1):
        #         st[i].next = st[i+1]
        #         i += 1
        #     st[i].next = None
        #     for i in st:
        #         if(i.left):
        #             q.append(i.left)
        #         if(i.right):
        #             q.append(i.right)
        #     st = q
        # return root
        
        # O(N),O(1)
        if(not root):
            return root
        leftmost = root
        
        while(leftmost.left):
            
            head = leftmost
            while(head):
                head.left.next = head.right
                if(head.next):
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
            

# first approach is simple as level order traversing

# second approach is tough
# don't forgot its given we have perfect binary tree
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solution/
# good explanation
                
        