class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        internal_degree = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            internal_degree[course] += 1

        query = [i for i, x in enumerate(internal_degree) if x == 0]
        for j in query:
            numCourses -= 1
            for k in graph[j]:
                internal_degree[k] -= 1
                if internal_degree[k] == 0:
                    query.append(k)

        return numCourses == 0
