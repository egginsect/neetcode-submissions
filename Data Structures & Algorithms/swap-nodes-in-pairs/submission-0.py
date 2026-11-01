# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            newhead = head.next
            head.next = self.swapPairs(head.next.next)
            newhead.next = head
            head = newhead
        return head 