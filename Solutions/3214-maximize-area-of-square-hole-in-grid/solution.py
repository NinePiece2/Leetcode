class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def counter(nums: List[int]):
            nums.sort()
            result = count = 1
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                    result = max(result, count)
                else:
                    count = 1
            return result + 1
        
        return min(counter(hBars), counter(vBars)) ** 2
