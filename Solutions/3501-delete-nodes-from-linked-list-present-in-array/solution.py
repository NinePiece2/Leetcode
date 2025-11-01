# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_nums = set(nums)
        dummy = last = ListNode(next=head)
        while last.next:
            if last.next.val in set_nums:
                last.next = last.next.next
            else:
                last = last.next
        return dummy.next
