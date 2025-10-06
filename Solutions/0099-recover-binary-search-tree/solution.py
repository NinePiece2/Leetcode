# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        last = first = second = None
        
        def dfs(root):
            if root is None:
                return

            nonlocal last, first, second
            dfs(root.left)
            if last and last.val > root.val:
                if first is None:
                    first = last
                second = root
            last = root
            dfs(root.right)

        dfs(root)
        first.val, second.val = second.val, first.val
