# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], arr):
            if root.left == root.right:
                arr.append(root.val)
                return
            
            if root.left:
                dfs(root.left, arr)
            if root.right:
                dfs(root.right, arr)

        arr1 = []
        arr2 = []
        dfs(root1, arr1)
        dfs(root2, arr2)
        return arr1 == arr2

