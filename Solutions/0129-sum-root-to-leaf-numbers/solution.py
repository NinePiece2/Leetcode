# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sum_val):
            if root is None:
                return 0
            sum_val = sum_val * 10 + root.val

            if root.left is None and root.right is None:
                return sum_val

            return dfs(root.left, sum_val) + dfs(root.right, sum_val)

        return dfs(root, 0)
