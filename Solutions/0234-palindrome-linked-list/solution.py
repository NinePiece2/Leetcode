# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        # last, current = None, slow.next

        # while current:
        #     tmp = current.next
        #     current.next = last
        #     last, current = current, tmp

        # while last:
        #     if last.val != head.val:
        #         return False
        #     last, head = last.next, head.next
        
        # return True

        dummy = head
        nums = []
        while dummy:
            nums.append(dummy.val)
            dummy = dummy.next
        return nums == nums[::-1]
