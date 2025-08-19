# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            dep = 0
            while root:
                dep += 1
                root = root.left
            return dep
        
        if root == None:
            return 0

        left, right = depth(root.left), depth(root.right)

        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)
