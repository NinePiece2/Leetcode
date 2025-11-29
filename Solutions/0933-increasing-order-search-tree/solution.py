# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = last = TreeNode(right=root)
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            nonlocal last
            dfs(root.left)
            last.right = root
            root.left = None
            last = root
            dfs(root.right)

        dfs(root)
        return dummy.right
