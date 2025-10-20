# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                result = head
                while result != slow:
                    result = result.next
                    slow = slow.next
                return result

        # visited = set()
        # current = head
        # while current:
        #     if current in visited:
        #         return current
        #     visited.add(current)
        #     current = current.next
        # return None
