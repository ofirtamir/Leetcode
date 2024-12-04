# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # q = deque()
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     if node:
        #         if node.left and node.val<=node.left.val:
        #             return False
        #         if node.right and node.val>=node.right.val:
        #             return False
        #         q.append(node.left)
        #         q.append(node.right)
        # return True
        def check(node, left,right):
            if not node:
                return True
            if not(node.val> left and node.val<right):
                return False
            return check(node.left, left,node.val) and check(node.right,node.val,right)
        return check(root, float('-inf'), float('inf'))