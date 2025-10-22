class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = defaultdict(int)
        table = defaultdict(int)

        for num in nums:
            count[num] += 1
            table[num] += 0
            table[num - k] += 1
            table[num + k + 1] -= 1
        
        result = sum_val = 0
        for val, occ in sorted(table.items()):
            sum_val += occ
            result = max(result, min(sum_val, count[val] + numOperations))

        return result
