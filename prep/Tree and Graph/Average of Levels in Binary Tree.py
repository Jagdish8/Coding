# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        if(not root):
            return ans
        
        q = [root]
        
        while(q):
            
            n = len(q)
            s = 0
            
            for i in range(n):
                
                node = q.pop(0)
                s += node.val
                
                if(node.right):
                    q.append(node.right)
                if(node.left):
                    q.append(node.left)
                    
            ans.append(s/n)
            
        return ans
            
        