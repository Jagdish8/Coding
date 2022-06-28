# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if(k == 0):
            return [target.val]
        self.parent = {}
        
        def storeParents(root):
            if(not root):
                return
            if(root.left):
                self.parent[root.left] = root
                storeParents(root.left)
            if(root.right):
                self.parent[root.right] = root
                storeParents(root.right)


            
        storeParents(root)
        q = [target]
        ans = []
        vis = set()
        while(q):
            # print(q)
            n = len(q)
            while(n):
                n -= 1
                node = q.pop(0)
                vis.add(node)
                if(k == 0):
                    ans.append(node.val)
                else:
                    if(node.left and node.left not in vis):
                        q.append(node.left)
                    if(node.right and node.right not in vis):
                        q.append( node.right)
                    if(node in self.parent and self.parent[node] not in vis):
                        q.append(self.parent[node])
            if(k == 0):
                return ans

            k -= 1
            
        return ans
                

# using bfs and also storing parent of each node in hashmap for going backwards
        