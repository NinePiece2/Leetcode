# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ListNode(0, head)
        last, current = pointer, head
        while current and current.next:
            node = current.next
            current.next = node.next
            node.next = current

            last.next = node
            last, current = current, current.next
        return pointer.next
