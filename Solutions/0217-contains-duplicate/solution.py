class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        # return True if any(i > 1 for val, i in count.items()) else False
        nums_set = set(nums)

        if len(nums) == len(nums_set):
            return False
        return True

        
