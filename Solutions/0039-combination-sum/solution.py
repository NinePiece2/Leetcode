class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, sum_val: int):
            if sum_val == 0:
                results.append(tmp[:])
            if sum_val < candidates[i]:
                return
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                dfs(j, sum_val - candidates[j])
                tmp.pop()

        candidates.sort()
        results = []
        tmp = []
        
        dfs(0, target)

        return results
