# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if(not root):
            return []
        
        ans = []
        q = [root]
        
        while(q):
            temp_ans = []
            temp_q = []
            while(q):
                node = q.pop(0)
                if(node.left):
                    temp_q.append(node.left)
                if(node.right):
                    temp_q.append(node.right)
                temp_ans.append(node.val)
            ans.append(temp_ans)
            q = temp_q
        
        return ans[::-1]
        