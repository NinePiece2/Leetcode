# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs approach
        # def check(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #     if root1 is None or root2 is None:
        #         return root1 is root2
        #     return (root1.val == root2.val and check(root1.left, root2.left) and 
        #             check(root1.right, root2.right))
        
        # if root is None:
        #     return False
        
        # return (check(root, subRoot) or self.isSubtree(root.left, subRoot) or 
        #         self.isSubtree(root.right, subRoot))

        # Hash Map / String Approach
        def encode(node: Optional[TreeNode]) -> str:
            if node is None:
                return ","
            return f"^{node.val}|{encode(node.left)}|{encode(node.right)}"

        root_str = encode(root)
        subRoot_str = encode(subRoot)

        return subRoot_str in root_str
