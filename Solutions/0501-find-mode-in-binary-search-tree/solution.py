# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        last = None
        max_val = count = 0
        result = []

        def dfs(root):
            if root is None:
                return 
            
            nonlocal max_val, count, last, result
            dfs(root.left)
            count = count + 1 if last == root.val else 1

            if count > max_val:
                result = [root.val]
                max_val = count
            elif count == max_val:
                result.append(root.val)
            last = root.val
            dfs(root.right)
        
        dfs(root)
        return result
