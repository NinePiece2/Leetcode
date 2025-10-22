# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        dummy = ListNode(next=head)
        last = dummy
        for _ in range(left - 1):
            last = last.next

        head1, head2 = last, last.next
        current = head2
        for _ in range(right - left + 1):
            temp = current.next
            current.next = last
            last, current = current, temp

        head1.next = last
        head2.next = current
        return dummy.next
