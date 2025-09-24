# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            val = postorder[j + n - 1]
            k = hash_table[val]
            left = dfs(i, j, k - i)
            right = dfs(k + 1, j + k - i, n - k + i - 1)
            
            return TreeNode(val, left, right)

        hash_table = {val: i for i, val in enumerate(inorder)}
        return dfs(0, 0, len(inorder))
