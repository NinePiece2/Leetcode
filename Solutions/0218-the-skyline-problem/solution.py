from queue import PriorityQueue

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        lines = []
        priority_queue = PriorityQueue()
        city, n = 0, len(buildings)

        for building in buildings:
            lines.extend([building[0], building[1]])
        lines.sort()

        for line in lines:
            while city < n and buildings[city][0] <= line:
                priority_queue.put([-buildings[city][2], buildings[city][0], buildings[city][1]])
                city += 1

            while not priority_queue.empty() and priority_queue.queue[0][2] <= line:
                priority_queue.get()
            
            height = 0
            if not priority_queue.empty():
                height = -priority_queue.queue[0][0]

            if len(skyline) > 0 and skyline[-1][1] == height:
                continue
            skyline.append([line, height])

        return skyline
