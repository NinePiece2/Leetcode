# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            pointer = ListNode(0)
            current = head
            while current:
                next_node = current.next
                current.next = pointer.next
                pointer.next = current
                current = next_node
            return pointer.next
        
        pointer = previous = ListNode(0, head)
        while previous:
            current = previous
            for i in range (k):
                current = current.next
                if current is None:
                    return pointer.next
            node = previous.next
            next_node = current.next
            current.next = None
            previous.next = reverse(node)
            node.next = next_node
            previous = node
        
        return pointer.next
