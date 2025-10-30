class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # return target[0] + sum(max(0, val2 - val1) for val1, val2 in pairwise(target))
        n = len(target)
        initial = [0] * n
        current = target[0]
        for i in range(1, n):
            if target[i] > target[i - 1]:
                current += target[i] - target[i - 1]

        return current
