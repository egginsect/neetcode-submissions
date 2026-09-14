# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None
        if l1:
            carry += l1.val
        if l2:
            carry += l2.val
        node = ListNode(carry%10)
        carry = carry//10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        node.next = self.addTwoNumbers(l1, l2, carry)
        return node