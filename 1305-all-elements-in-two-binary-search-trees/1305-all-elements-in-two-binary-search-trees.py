# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        def dfs(root, arr):
            arr = dfs(root.left, arr) + [root.val] + dfs(root.right, arr) if root else []
            return arr
        
        arr = dfs(root1, arr)
        arr.extend(dfs(root2, arr))
        return sorted(arr)