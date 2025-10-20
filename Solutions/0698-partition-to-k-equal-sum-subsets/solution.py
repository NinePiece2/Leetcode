class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        
        nums.sort()
        mask = (1 << len(nums)) - 1

        @cache
        def dfs(state, temp):
            if state == mask:
                return True
            for i, num in enumerate(nums):
                if (state >> i) & 1:
                    continue
                if temp + num > s:
                    break
                if dfs(state | 1 << i, (temp + num) % s):
                    return True
            return False
        
        return dfs(0, 0)
