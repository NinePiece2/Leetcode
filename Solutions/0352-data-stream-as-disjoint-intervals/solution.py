class SummaryRanges:

    def __init__(self):
        self.map = SortedDict()

    def addNum(self, value: int) -> None:
        n = len(self.map)
        right_index = self.map.bisect_right(value)
        left_index = n if right_index == 0 else right_index - 1

        keys = self.map.keys()
        values = self.map.values()

        if (right_index != n and left_index != n and 
                values[right_index][0] - 1 == value and values[left_index][1] + 1 == value):
            self.map[keys[left_index]][1] = self.map[keys[right_index]][1]
            self.map.pop(keys[right_index])
        elif left_index != n and values[left_index][1] + 1 >= value:
            self.map[keys[left_index]][1] = max(value, self.map[keys[left_index]][1])
        
        elif right_index != n and values[right_index][0] - 1 <= value:
            self.map[keys[right_index]][0] = min(value, self.map[keys[right_index]][0])
        
        else:
            self.map[value] = [value, value]

    def getIntervals(self) -> List[List[int]]:
        return list(self.map.values())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
