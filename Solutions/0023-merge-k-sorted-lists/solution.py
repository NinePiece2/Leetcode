# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Need to att a comparison method for the heap
        # to avoid TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        # lt is less than (<)
        setattr(ListNode, '__lt__', lambda a, b: a.val < b.val)
        heap = [head for head in lists if head]

        heapify(heap)
        pointer = current = ListNode()
        while heap:
            node = heappop(heap)
            if node.next:
                heappush(heap, node.next)
            current.next = node
            current = current.next
        return pointer.next
