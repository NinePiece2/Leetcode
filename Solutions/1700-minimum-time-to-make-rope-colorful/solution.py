class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        result = i = 0
        while i < n:
            j = i
            sum_val = max_val = 0
            while j < n and colors[i] == colors[j]:
                sum_val += neededTime[j]
                if max_val < neededTime[j]:
                    max_val = neededTime[j]
                j += 1
            result += sum_val - max_val
            i = j
        
        return result
