# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum_val):
            if root is None:
                return False
            sum_val += root.val
            if root.left is None and root.right is None and sum_val == targetSum:
                return True
            return dfs(root.left, sum_val) or dfs(root.right, sum_val)
        
        return dfs(root, 0)
