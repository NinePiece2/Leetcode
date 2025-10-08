class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # max_num = max(count.values())
        # return next(key for key, val in count.items() if val == max_num)

        # nums = sorted(nums)
        # return nums[len(nums)//2]

        count = maj = 0
        for num in nums:
            if count == 0:
                maj, count = num, 1
            else:
                count += 1 if num == maj else -1

        return maj
