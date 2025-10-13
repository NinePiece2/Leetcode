"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # result = []
        # def dfs(root):
        #     if root is None:
        #         return
        #     for child in root.children:
        #         dfs(child)
        #     result.append(root.val)
        #     return

        # dfs(root)
        # return result

        result = []
        if root is None:
            return result

        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in node.children:
                stack.append(child)

        return result[::-1]
