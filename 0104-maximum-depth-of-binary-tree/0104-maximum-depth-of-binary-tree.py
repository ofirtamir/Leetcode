# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root == None :
        #     return 0
        # return max(1+ self.maxDepth(root.left), 1+ self.maxDepth(root.right))
        
        #by bfs
        if root ==None:
            return 0
        res = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res+=1
        return res               
