class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        operators = ('+', '-', '*', '/')
        nums = [float(num) for num in cards]

        def dfs(curr_nums: List[float]):
            n = len(curr_nums)
            if n == 1:
                if abs(curr_nums[0] - 24) < 1e-4:
                    return True
                return False

            good = False
            for i in range(n):
                for j in range(n):
                    if i != j:
                        next_num = [curr_nums[k] for k in range(n) if k != i and k != j]
                        for op in operators:
                            match op:
                                case "/":
                                    if curr_nums[j] == 0:
                                        continue
                                    good |= dfs(next_num + [curr_nums[i] / curr_nums[j]])
                                case "*":
                                    good |= dfs(next_num + [curr_nums[i] * curr_nums[j]])
                                case "+":
                                    good |= dfs(next_num + [curr_nums[i] + curr_nums[j]])
                                case "-":
                                    good |= dfs(next_num + [curr_nums[i] - curr_nums[j]])
                            if good:
                                return True
            return good
        
        return dfs(nums)
