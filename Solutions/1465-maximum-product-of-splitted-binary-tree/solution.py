# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7

        def tree_sum(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return root.val + tree_sum(root.left) + tree_sum(root.right)

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            tmp = root.val + dfs(root.left) + dfs(root.right)
            nonlocal result
            if tmp < total_sum:
                result = max(result, tmp * (total_sum - tmp))
            return tmp
        
        total_sum = tree_sum(root)
        result = 0
        dfs(root)
        return result % mod
