"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [(1,root)]
        max_depth = 1
        while stack:
            depth, parent = stack.pop()
            x = parent.children
            if not any(x):
                max_depth = max(max_depth,depth)
            for i in x:
                if i:
                    stack.append((depth+1,i))
        return max_depth
            