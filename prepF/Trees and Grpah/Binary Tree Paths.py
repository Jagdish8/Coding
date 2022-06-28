# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        
        def solve(root,path):
            if(root):
                if(not root.left and not root.right):
                        if(path):
                            self.ans.append(path + "->" + str(root.val))
                        else:
                            self.ans.append(path + str(root.val))
                        return
                if(path):
                    solve(root.left,path + "->" + str(root.val))
                    solve(root.right,path + "->" + str(root.val))
                else:
                    solve(root.left,path + str(root.val))
                    solve(root.right,path + str(root.val))

        solve(root,"")
        return self.ans

# similar approach as preorder traversal
        