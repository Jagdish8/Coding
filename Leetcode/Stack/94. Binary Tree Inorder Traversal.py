# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        st=[]
        ans=[]
        while(root):
            st.append(root)
            root= root.left
        while(st):
            p = st.pop()
            ans.append(p.val)
            x = p.right
            while(x):
                st.append(x)
                x = x.left
        return ans
        