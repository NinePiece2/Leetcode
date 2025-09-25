class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == len(nums):
                result.append(temp[:])
                return 
            temp.append(nums[i])
            dfs(i + 1)
            val = temp.pop()
            while i + 1 < len(nums) and nums[i + 1] == val:
                i += 1

            dfs(i + 1)

        nums.sort()
        result = []
        temp = []
        dfs(0)

        return result
