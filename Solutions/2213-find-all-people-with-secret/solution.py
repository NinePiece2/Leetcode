class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        visited = [False] * n
        visited[0] = visited[firstPerson] = True
        meetings.sort(key=lambda x: x[2])
        i, m = 0, len(meetings)
        while m > i:
            j = i
            while j + 1 < m and meetings[j + 1][2] == meetings[i][2]:
                j += 1
            s = set()
            graph = defaultdict(list)
            for x, y, _ in meetings[i : j + 1]:
                graph[x].append(y)
                graph[y].append(x)
                s.update([x, y])
            queue = deque([u for u in s if visited[u]])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            i = j + 1

        return [i for i, val in enumerate(visited) if val]
