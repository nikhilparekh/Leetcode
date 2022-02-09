# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            return dfs(root.left)+[root.val]+dfs(root.right) if root else []
        res = dfs(root)
        cmin = max(res)
        for i in range(1,len(res)):
            cmin = min(cmin,abs(res[i]-res[i-1]))
        return cmin