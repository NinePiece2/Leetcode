class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        nums = [0] * n
        val = 0
        for j, (i, colour) in enumerate(queries):
            if i > 0 and nums[i] and nums[i - 1] == nums[i]:
                val -= 1
            if i < n - 1 and nums[i] and nums[i + 1] == nums[i]:
                val -= 1
            if i > 0 and nums[i - 1] == colour:
                val += 1
            if i < n - 1 and nums[i + 1] == colour:
                val += 1
            result[j] = val
            nums[i] = colour
        return result
