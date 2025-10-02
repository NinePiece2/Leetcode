class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        words = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        index = list(range(n))
        index.sort(key=lambda x : -score[x])
        result = [None] * n

        for i, val in enumerate(index):
            result[val] = words[i] if i < 3 else str(i + 1)
        
        return result
