class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, val in enumerate(groupSizes):
            groups[val].append(i)
        result = [val[j : j + i] for i, val in groups.items() for j in range(0, len(val), i)]

        return result
