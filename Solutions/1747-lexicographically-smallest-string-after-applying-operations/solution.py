class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        visited = set(s)
        result = s

        while queue:
            s = queue.popleft()
            if result > s:
                result = s
            temp = "".join([str((int(char) + a) % 10) if i & 1 else char for i, char in enumerate(s)])
            temp2 = s[-b:] + s[:-b]

            for t in (temp, temp2):
                if t not in visited:
                    visited.add(t)
                    queue.append(t)

        return result
