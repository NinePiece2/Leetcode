# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent):
            if root is None:
                return
            dic[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)

        def dfs2(root, parent, k):
            if root is None:
                return 0
            if k == 0:
                result.append(root.val)
                return
            
            for nxt in (root.left, root.right, dic[root]):
                if nxt != parent:
                    dfs2(nxt, root, k - 1)
        
        dic = {}
        dfs(root, None)
        result = []
        dfs2(target, None, k)

        return result
