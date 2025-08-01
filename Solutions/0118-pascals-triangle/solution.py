class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = []
        for i in range(numRows):
            current = [1] * (i + 1)

            for j in range(1, i):
                current[j] = solution[i - 1][j - 1] + solution[i - 1][j]

            solution.append(current)
        return solution
