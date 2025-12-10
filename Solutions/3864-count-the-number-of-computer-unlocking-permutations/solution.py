class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        result = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            result = result * i % (10**9 + 7)
        return result
