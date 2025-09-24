class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = list(accumulate(nums, initial=0))
        sorted_array = sorted(set(val for x in n for val in (x, x - lower, x - upper)))
        tree = BinaryIndexedTree(len(sorted_array))
        result = 0

        for x in n:
            left = bisect_left(sorted_array, x - upper) + 1
            right = bisect_left(sorted_array, x - lower) + 1
            result += tree.query(right) - tree.query(left - 1)
            tree.update(bisect_left(sorted_array, x) + 1, 1)

        return result

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, x, v):
        while x <= self.n:
            self.tree[x] += v
            x += x & -x
    
    def query(self, x):
        result = 0
        while x > 0:
            result += self.tree[x]
            x -= x & -x
        return result
