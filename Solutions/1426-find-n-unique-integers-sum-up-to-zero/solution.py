class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = list(range(1, n))
        result.append(-sum(result))

        return result
