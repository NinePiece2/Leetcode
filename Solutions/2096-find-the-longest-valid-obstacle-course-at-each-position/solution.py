# class BinaryIndexedTree:
#     def  __init__ (self, n: int):
#         self.n = n
#         self.tree = [0] * (n + 1)
    
#     def update(self, index: int, val: int):
#         while index <= self.n:
#             self.tree[index] = max(self.tree[index], val)
#             index += index & -index
    
#     def query(self, index: int):
#         result = 0
#         while index:
#             result = max(self.tree[index], result)
#             index -= index & -index
#         return result

# class Solution:
#     def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
#         nums = sorted(set(obstacles))
#         n = len(nums)

#         tree = BinaryIndexedTree(n)
#         result = []
#         for val in obstacles:
#             idx = bisect_left(nums, val) + 1
#             result.append(tree.query(idx) + 1)
#             tree.update(idx, result[-1])
#         return result

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        count = 0
        dp, result = [], []

        for ob in obstacles:
            if not dp or ob >= dp[-1]:
                dp.append(ob)
                count += 1
                result.append(count)
            else:
                idx = bisect_right(dp, ob)
                dp[idx] = ob
                result.append(idx + 1)
        return result
