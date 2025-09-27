# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        val1 = val2 = list1
        for _ in range(a - 1):
            val1 = val1.next

        for _ in range(b):
            val2 = val2.next

        val1.next = list2
        while val1.next:
            val1 = val1.next

        val1.next = val2.next
        val2.next = None

        return list1
