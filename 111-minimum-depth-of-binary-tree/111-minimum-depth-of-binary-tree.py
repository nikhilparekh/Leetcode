# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1,root)]
        md = float("inf")
        while stack:
            depth, root = stack.pop()
            children = [root.left,root.right]
            if not any(children):
                md = min(depth,md)
            for i in children:
                if i:
                    stack.append((depth+1,i))
        return md