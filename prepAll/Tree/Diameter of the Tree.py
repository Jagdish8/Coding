from logging import root
from readline import read_history_file
from turtle import right
from xml.dom.minicompat import NodeList


diameter of the tree is the longest path between 2 nodes
the path does not need to be pass via the root

brute : O(N**2)
    first we start with root
    check lh and rh for the root
    now get max of ans,lh+rh
    then we call for left and right
    and do the same

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        if(not root):
            return 0
        def heigth(root):  (O(N))
            if(not root):
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return 1 + max(lh,rh)
        def solve(root):
            if(not root):
                return 0
            lh = heigth(root.left)
            rh = heigth(root.right)
            self.d = max(self.d,lh+rh)
            solve(root.left)   (O(N))
            solve(root.right)   (O(N))
        solve(root)
        return self.d

Efficient way: (O(n))

    Instead if calculating for all root.left and all root.right
    we can do modification in the finding height it self, since we calculate the 
    heights of all in there

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        if(not root):
            return 0
        def solve(root):
            if(not root):
                return 0
            lh = solve(root.left)
            rh = solve(root.right)
            self.d = max(self.d,lh+rh)
            return  1 + max(lh,rh)
        solve(root)
        return self.d