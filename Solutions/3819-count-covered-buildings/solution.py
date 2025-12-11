class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_graph = defaultdict(list)
        y_graph = defaultdict(list)
        for x, y in buildings:
            x_graph[x].append(y)
            y_graph[y].append(x)
        for x in x_graph:
            x_graph[x].sort()
        for y in y_graph:
            y_graph[y].sort()

        result = 0
        for x, y in buildings:
            x_list, y_list = x_graph[x], y_graph[y]
            if y_list[0] < x < y_list[-1] and x_list[0] < y < x_list[-1]:
                result += 1
        return result
