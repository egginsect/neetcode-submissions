# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1, 2, 3, 4
              v
        c     v
           c     v
              c.    v      
        """
        dummy = ListNode(0, head)
        fast = head
        for _ in range(n):
            fast  = fast.next

        slow = dummy
        while slow and fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next