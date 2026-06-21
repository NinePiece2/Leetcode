from collections import OrderedDict

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dict = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.dict:
#             return -1
#         self.dict.move_to_end(key, last=True)
#         return self.dict[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.dict:
#             self.dict.move_to_end(key, last=True)
        
#         self.dict[key] = value
        
#         if len(self.dict) > self.capacity:
#             self.dict.popitem(last=False)

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        
        self.head = Node() # LRU End/Oldest
        self.tail = Node() # Most Recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_at_tail(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_tail(node)
        return node.value
    
    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]

        node = Node(key, val)
        self.cache[key] = node
        self._insert_at_tail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            if lru != self.tail:
                self._remove(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
