# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # עץ ריק תמיד תת-עץ
            return True
        if not root:  # אם root ריק אך subRoot לא, הוא לא יכול להיות תת-עץ
            return False
        
        # בדיקה אם העצים שווים מתחילתם
        if self.isSameTree(root, subRoot):
            return True
        
        # בדיקה בתת-העצים של root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # שני העצים ריקים
            return True
        if not p or not q:  # אחד ריק והשני לא
            return False
        if p.val != q.val:  # הערכים שונים
            return False
        
        # בדיקה רקורסיבית עבור תת-העצים
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
