class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        result = 0
        happiness.sort(reverse=True)

        for i, val in enumerate(happiness[:k]):
            val -= i
            if val > 0:
                result += val

        return result
