class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, val):
        if self.p[val] != val:
            self.p[val] = self.find(self.p[val])
        return self.p[val]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        union_find = UnionFind(c + 1)
        for u, v in connections:
            union_find.union(u, v)
        
        sorted_list = [SortedList() for _ in range(c + 1)]
        for i in range(1, c + 1):
            sorted_list[union_find.find(i)].add(i)
        
        result = []
        for a, x in queries:
            root = union_find.find(x)
            if a == 1:
                if x in sorted_list[root]:
                    result.append(x)
                elif len(sorted_list[root]):
                    result.append(sorted_list[root][0])
                else:
                    result.append(-1)
            else:
                sorted_list[root].discard(x)
        
        return result
