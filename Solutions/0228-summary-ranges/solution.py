class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def formatter(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}"

        i, n = 0, len(nums)
        result = []

        while n > i:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            result.append(formatter(i, j))
            i = j + 1
        return result
