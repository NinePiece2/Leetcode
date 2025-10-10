class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash_map = defaultdict(list)
        index = [0] * numCourses
        for a, b in prerequisites:
            hash_map[b].append(a)
            index[a] += 1
        
        result = []
        queue = deque(i for i, val in enumerate(index) if val == 0)
        while queue:
            idx = queue.popleft()
            result.append(idx)
            for j in hash_map[idx]:
                index[j] -= 1
                if index[j] == 0:
                    queue.append(j)

        return result if len(result) == numCourses else []
