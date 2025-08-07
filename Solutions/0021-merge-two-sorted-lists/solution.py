# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_n = list1
        list2_n = list2
        result = pointer = ListNode()

        while list1_n and list2_n:
            if list1_n.val < list2_n.val:
                result.next = list1_n
                list1_n = list1_n.next
            else:
                result.next = list2_n
                list2_n = list2_n.next
            result = result.next

        result.next = list1_n if list1_n else list2_n

        return pointer.next


