# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        current, n = head, 0
        while current:
            n += 1
            current = current.next
        
        k %= n
        if k == 0:
            return head
        
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        
        result = slow.next
        slow.next = None
        fast.next = head
        return result
