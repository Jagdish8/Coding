# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example 2:


# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example 3:


# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if(not root):
            return []
        
        self.ans = {}
        

        # dfs gives ordering wrong for a perticular vertical line
        
        # it goes first to left and does everything there first so for all vertices from left 
        # all will be added first, later when we go to right, the one which should be above is appended below


        # def solve(root,key):
        #     if(not root):
        #         return
        #     if(key not in self.ans):
        #         self.ans[key] = []
        #     self.ans[key].append(root.val)
        #     print(self.ans)
        #     solve(root.left,key-1)
        #     solve(root.right,key+1)
            
        # solve(root,0)


        #bfs approach
        q = [[root,0]]
        while(q):
            # print(q)
            n = len(q)
            while(n):
                n -= 1
                node,key = q.pop(0)
                if(key not in self.ans):
                    self.ans[key] = []
                self.ans[key].append(node.val)
                if(node.left):
                    q.append([node.left,key-1])
                if(node.right):
                    q.append([node.right,key+1])
        
        ans = []

        for i in sorted(self.ans.keys()):
            ans.append(self.ans[i])
        return ans