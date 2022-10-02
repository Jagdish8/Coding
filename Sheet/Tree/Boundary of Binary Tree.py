# https://leetcode.com/problems/boundary-of-binary-tree/

# The boundary of a binary tree is the concatenation of the root, the left boundary,
# the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree.
# Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        self.left = []
        temp = root
        if(not temp.left):
            self.left.append(root)
        else:
            while(temp):
                self.left.append(temp)
                if(temp.left):
                    temp = temp.left
                else:
                    temp = temp.right
                    
        
        self.right = []
        temp = root
        if(not temp.right):
            self.left.append(root)
        else:
            while(temp):
                self.right.append(temp)
                if(temp.right):
                    temp = temp.right
                else:
                    temp = temp.left
        
        
        self.leaves = []
        def leaves(root):
            if(not root):
                return
            if(not root.left and not root.right):
                self.leaves.append(root)
            leaves(root.left)
            leaves(root.right)
        leaves(root)
        
        nodes = self.left + self.leaves + self.right[::-1]
        vis = set()
        res = []
        for i in nodes:
            if(i not in vis):
                res.append(i.val)
                vis.add(i)
                
        return res
            
# find left
# find right
# find all leaves

# then append all distinct
        
