class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        result = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - i - 1] = boxGrid[i][j]

        for j in range(m):
            queue = Deque()
            for i in range(n - 1, -1, -1):
                if result[i][j] == "*":
                    queue.clear()
                elif result[i][j] == ".":
                    queue.append(i)
                elif queue:
                    result[queue.popleft()][j] = "#"
                    result[i][j] = "."
                    queue.append(i)
        
        return result

