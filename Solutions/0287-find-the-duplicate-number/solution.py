class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def keyfunc(i: int) -> bool:
            return sum(x <= i for x in nums) > i
        
        return bisect_left(range(len(nums)), True, key=keyfunc)
