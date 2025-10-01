class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, last, temp):
            if i == len(nums):
                if len(temp) > 1:
                    result.append(temp[:])
                return

            if nums[i] >= last:
                temp.append(nums[i])
                dfs(i + 1, nums[i], temp)
                temp.pop()

            if nums[i] != last:
                dfs(i + 1, last, temp)

        
        dfs(0, -101, [])
        return result
