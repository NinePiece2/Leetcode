# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        last = float('-inf')
        result = float('inf')

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal last, result
            result = min(result, root.val - last)
            last = root.val
            dfs(root.right)
        
        dfs(root)
        return result
