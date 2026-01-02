class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # n = len(nums) // 2
        # count = Counter(nums)

        # for val, cnt in count.items():
        #     if cnt == n:
        #         return val
        vis = set()
        for i in nums:
            if i in vis:
                return i
            vis.add(i)
            
