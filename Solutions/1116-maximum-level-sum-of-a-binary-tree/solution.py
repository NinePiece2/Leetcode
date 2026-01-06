# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # val_set = defaultdict(int)
        
        # def dfs(root: Optional[TreeNode], level: int):
        #     if root is None:
        #         return
        #     dfs(root.left, level + 1)
        #     val_set[level] += root.val
        #     dfs(root.right, level + 1)
        #     return
        
        # dfs(root, 1)
        # print(val_set)

        # sum_val = float('-inf')
        # result = 1
        # for i, val in val_set.items():
        #     if val > sum_val or (val == sum_val and i < result):
        #         result = i
        #         sum_val = val
        # return result
        
        curr_level = min_level = 1
        max_sum = float('-inf')
        queue = deque()
        queue.append(root)

        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_level = curr_level
            curr_level += 1
        
        return min_level
