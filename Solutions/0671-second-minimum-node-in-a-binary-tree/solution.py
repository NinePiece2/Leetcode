# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result, val = -1, root.val
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                nonlocal result, val
                if root.val > val:
                    result = root.val if result == -1 else min(result, root.val)
        dfs(root)
        return result
