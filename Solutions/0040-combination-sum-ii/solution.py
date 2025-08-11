class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, sum_val: int):
            if sum_val == 0:
                results.append(tmp[:])
            if i >= len(candidates) or sum_val < candidates[i]:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                tmp.append(candidates[j])
                dfs(j + 1, sum_val - candidates[j])
                tmp.pop()

        candidates.sort()
        results = []
        tmp = []
        
        dfs(0, target)

        return results
