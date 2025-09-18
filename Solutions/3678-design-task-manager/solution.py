class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.hash_table = {}
        self.sorted_list = SortedList()
        for task in tasks:
            self.add(*task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.hash_table[taskId] = (userId, priority)
        self.sorted_list.add((-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.hash_table[taskId]
        self.sorted_list.remove((-priority, -taskId))
        self.hash_table[taskId] = (userId, newPriority)
        self.sorted_list.add((-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        _, priority = self.hash_table[taskId]
        self.hash_table.pop(taskId)
        self.sorted_list.remove((-priority, -taskId))

    def execTop(self) -> int:
        if not self.sorted_list:
            return -1
        taskId = -self.sorted_list.pop(0)[1]
        userId, _ = self.hash_table[taskId]
        self.hash_table.pop(taskId)
        
        return userId
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
