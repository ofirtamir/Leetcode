# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxde=0
        def dia(root):
            if not root:
                return 0
            x= dia(root.left)
            y= dia(root.right)
            self.maxde= max(self.maxde,x+y)
            return max(x,y)+1
        dia(root)
        return self.maxde

