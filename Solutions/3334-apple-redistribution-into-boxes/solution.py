class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort()
        capacity = capacity[::-1]
        i = 0

        while total_apples > 0:
            total_apples -= capacity[i]
            i += 1

        return i
