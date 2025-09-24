# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            val = preorder[i]
            k = hash_table[val]
            left = dfs(i + 1, j, k - j)
            right = dfs(i + 1 + k - j, k + 1, n - k + j - 1)
            
            return TreeNode(val, left, right)

        hash_table = {val: i for i, val in enumerate(inorder)}
        return dfs(0, 0, len(preorder))
