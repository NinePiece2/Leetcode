class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        highest = max(count.values())
        total = sum(highest == i for i in count.values())

        return max(len(tasks), (highest - 1) *  (n + 1) + total)
