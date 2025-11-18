# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        temp_right, temp_left = right, left
        while head:
            if head.val < x:
                temp_left.next = head
                temp_left = temp_left.next
            else:
                temp_right.next = head
                temp_right = temp_right.next
            head = head.next
        
        temp_right.next = None
        temp_left.next = right.next
        return left.next
