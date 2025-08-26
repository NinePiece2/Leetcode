class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        result = max_diag = 0
        for length, width in dimensions:
            tmp = sqrt(length**2 + width**2)
            if max_diag < tmp:
                max_diag = tmp
                result = length * width
            elif max_diag == tmp:
                result = max(result, length * width)

        return result
