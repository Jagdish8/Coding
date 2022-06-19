# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self, root: 'Node') -> List[int]:
        if(not root):
            return []
        def solve(root):
            # print(root)
            if(root):
                for i in root:
                    self.ans.append(i.val)
                    solve(i.children)
        self.ans.append(root.val)
        solve(root.children)
        return self.ans
            
# children are stored in list and root.children is pointed to that list
        