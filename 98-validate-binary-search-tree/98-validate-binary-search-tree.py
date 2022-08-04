# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, res):
            if not root:
                return None
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right, res)
            return res
    
        x = dfs(root,[])
        prev = x[0]
        for i in x[1:]:
            if prev>=i:
                return False
            prev=i
        return True