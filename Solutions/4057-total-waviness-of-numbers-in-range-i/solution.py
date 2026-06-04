class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def sim(val: int) -> int:
            nums = []
            while val:
                nums.append(val % 10)
                val //= 10
            n = len(nums)
            if n < 3:
                return 0
            sum_val = 0
            for i in range(1, n - 1):
                if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                    # peak
                    sum_val += 1
                elif nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
                    # valley
                    sum_val += 1
            return sum_val

        return sum(sim(val) for val in range(num1, num2 + 1))
