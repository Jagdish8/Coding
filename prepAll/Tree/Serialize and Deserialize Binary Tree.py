# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        ans = []
        if(not root):
            return ""
        st = [root]
        level = 0
        while(st):
            q = []
            for i in st:
                if(i == None):
                    ans.append(str(None))
                    continue
                ans.append(str(i.val))
                q.append(i.left)
                q.append(i.right)
            st = q
        print(ans)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(not data):
            return None
        data = data.split(",")
        for i,j in enumerate(data):
            if(j == 'None'):
                data[i] = None
            else:
                data[i] = int(j)
        # print(data)
        root = TreeNode(data[0])
        q = [root]
        i = 1
        while(q and i<len(data)):
            # print(root)
            # print(q)
            node = q.pop(0)
            # print(node)
            if(data[i] != None):
                new = TreeNode(data[i])
                node.left = new
                q.append(new)
            i += 1
            if(data[i] != None):
                new = TreeNode(data[i])
                node.right = new
                q.append(new)
            i += 1
            # print(node)
        return root
                
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# using level order traversal approach