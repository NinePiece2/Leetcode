class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == len(nums):
                result.append(temp[:])
                return 
            dfs(i + 1)
            temp.append(nums[i])
            dfs(i + 1)
            temp.pop()

        result = []
        temp = []
        dfs(0)

        return result
