# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q= deque()
        q.append(root)
        res=[]
        val=[]
        # res.append(root.val)
        while q:
            val =[]
            lenq= len(q)
            for i in range(lenq):
                node =q.popleft()
                if node:
                    q.append(node.right)
                    q.append(node.left)
                    val.append(node.val)
            if val:
                res.append(val[0])
        return res