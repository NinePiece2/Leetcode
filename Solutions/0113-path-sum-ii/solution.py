# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        stack = []

        def dfs(root, sum_val):
            if root is None:
                return
            sum_val += root.val
            stack.append(root.val)
            if root.left is None and root.right is None and sum_val == targetSum:
                result.append(stack[:])
            
            dfs(root.left, sum_val)
            dfs(root.right, sum_val)
            stack.pop()
        
        dfs(root, 0)
        return result
