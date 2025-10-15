# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        last = float('inf')

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            nonlocal result, last
            result = min(result, abs(root.val - last))
            last = root.val
            dfs(root.right)
        
        dfs(root)
        return result
