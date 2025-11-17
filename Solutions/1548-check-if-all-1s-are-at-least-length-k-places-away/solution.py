class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # count = float('inf')
        # for num in nums:
        #     if num == 1:
        #         if count < k:
        #             return False
        #         count = 0
        #     else:
        #         count += 1
        # return True

        if k == 0:
            return True
        last = None
        for i, num in enumerate(nums):
            if num == 1:
                if last is not None and i - last <= k:
                    return False
                last = i
        return True
