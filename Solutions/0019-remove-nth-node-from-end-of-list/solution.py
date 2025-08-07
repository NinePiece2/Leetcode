# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        last = curr = temp

        for i in range(n + 1):
            curr = curr.next
        while curr:
            curr = curr.next
            last = last.next

        last.next = last.next.next
                
        return temp.next #head[n - 1].next = head[n].next
