# Given the root of a binary tree, turn the tree upside down and return the new root.

# You can turn a binary tree upside down with the following steps:

# The original left child becomes the new root.
# The original root becomes the new right child.
# The original right child becomes the new left child.

# The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: [4,5,2,null,null,3,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 10].
# 1 <= Node.val <= 10
# Every right node in the tree has a sibling (a left node that shares the same parent).
# Every right node in the tree has no children.



# https://leetcode.com/explore/interview/card/linkedin/341/trees-and-graphs/1984/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root or not root.left):
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newRoot
        

# similar to linked list reverse
# remember