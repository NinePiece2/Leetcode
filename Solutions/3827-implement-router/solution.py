from dataclasses import dataclass

@dataclass(frozen=True,eq=True)
class Packet:
    source: int
    destination: int
    timestamp: int

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.unique = set()

        self.dest_timestamps = defaultdict(list)
        self.forwarded_count = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = Packet(source, destination, timestamp)
        if packet in self.unique:
            return False
        if len(self.unique) == self.memoryLimit:
            self.forwardPacket()
        
        self.queue.append(packet)
        self.unique.add(packet)
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.unique.remove(packet)
        self.forwarded_count[packet.destination] += 1
        return [packet.source, packet.destination, packet.timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_timestamps.get(destination)
        if not timestamps:
            return 0
        removed = self.forwarded_count.get(destination, 0)
        high = bisect_right(timestamps, endTime, lo=removed)
        low = bisect_left(timestamps, startTime, lo=removed)
        return high - low

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
