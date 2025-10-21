# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        last = None

        while current:
            temp = current.next
            current.next = last
            last, current = current, temp
        current = head

        while last:
            temp = last.next
            last.next = current.next
            current.next = last
            current, last = last.next, temp
