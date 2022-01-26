"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            for i in root.children:
                self.postorder(i)
            self.res.append(root.val)
        return self.res