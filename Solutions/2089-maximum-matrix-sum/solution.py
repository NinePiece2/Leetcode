class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = negitives = 0
        min_val = float("inf")

        for row in matrix:
            for val in row:
                result += abs(val)
                if val < 0:
                    negitives += 1
                min_val = min(min_val, abs(val))

        if negitives % 2 != 0: #odd
            result -= min_val * 2

        return result
