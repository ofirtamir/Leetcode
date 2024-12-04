# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sub(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
    def sub(self,root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val !=subRoot.val:
            return False
        
        return True and self.sub(root.left,subRoot.left) and self.sub(root.right,subRoot.right)

        