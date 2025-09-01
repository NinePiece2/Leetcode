class BinaryTree:
    def __init__(self, num):
        self.n = num
        self.c = [0] * (num + 1)

    @staticmethod
    def lowbit(x):
        return x & -x
    
    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += BinaryTree.lowbit(x)
    
    def query(self, x):
        s = 0
        while x > 0:
            s += self.c[x]
            x -= BinaryTree.lowbit(x)
        return s

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        maped_nums = {val: i for i, val in enumerate(sorted_nums, 1)}
        tree = BinaryTree(len(maped_nums))
        result = []

        for val in nums[::-1]:
            x = maped_nums[val]
            tree.update(x, 1)
            result.append(tree.query(x - 1))
        
        return result[::-1]
