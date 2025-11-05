class Tree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)
    
    def maximize(self, i: int, val: int):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += Tree.lowtree(i)

    @staticmethod
    def lowtree(i: int) -> int:
        return i & -i
    
    def get(self, i: int) -> int:
        result = 0
        while i > 0:
            result = max(result, self.tree[i])
            i -= Tree.lowtree(i)
        return result

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = len(queries) * 3
        result = []
        tree = Tree(n + 1)
        obsticles = SortedList([0, n])

        for query in queries:
            if query[0] == 1:
                obsticles.add(query[1])

        for val1, val2 in pairwise(obsticles):
            tree.maximize(val2, val2 - val1)

        for query in reversed(queries):
            if query[0] == 1:
                val = query[1]
                i = obsticles.index(val)
                next_val = obsticles[i + 1]
                last_val = obsticles[i - 1]
                obsticles.remove(val)
                tree.maximize(next_val, next_val - last_val)
            else:
                val = query[1]
                sz = query[2]
                i = obsticles.bisect_right(val)
                last_val = obsticles[i - 1]
                result.append(tree.get(last_val) >= sz or val - last_val >= sz)

        return result[::-1]

