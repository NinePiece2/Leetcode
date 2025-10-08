# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        temp = []
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            temp.append(str(root.val))
            if root.left is None and root.right is None:
                result.append("->".join(temp))
            else:
                dfs(root.left)
                dfs(root.right)
            temp.pop()

        dfs(root)
        return result
