# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []

        while queue:
            sum_val, n = 0, len(queue)
            for _ in range(n):
                root = queue.popleft()
                sum_val += root.val

                if root.left:
                    queue.append(root.left)

                if root.right:
                    queue.append(root.right)

            result.append(sum_val / n)

        return result
