# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
    # Recursive
    def solve(root):
        if(root):
            self.ans.append(root.val)
            solve(root.left)
            solve(root.right)
        return None
    solve(root)
    return self.ans
    
    # Iterative
    if(not root):
        return []
    st = [root]
    while(st):
        # print(st)
        p = st.pop(0)
        self.ans.append(p.val)
        if(p.right):
            st = [p.right] + st
        if(p.left):
            st = [p.left] + st
    return self.ans

# do for all


    

            
        