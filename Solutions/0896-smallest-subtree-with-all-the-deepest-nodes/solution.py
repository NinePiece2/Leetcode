# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return subtree and depth
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return None, 0
            l, l_depth = dfs(root.left)
            r, r_depth = dfs(root.right)
            if l_depth > r_depth:
                return l, l_depth + 1
            if l_depth < r_depth:
                return r, r_depth + 1
            return root, l_depth + 1
        
        return dfs(root)[0]
            
