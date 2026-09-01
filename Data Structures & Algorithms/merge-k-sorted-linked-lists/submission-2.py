# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, l1, l2):
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val <= l2.val:
        #     node = l1
        #     node.next = self.merge(l1.next, l2)
        # else:
        #     node = l2
        #     node.next = self.merge(l1, l2.next)
        # return node

        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:
            if not l2:
                curr.next = l1
                l1 = l1.next
            elif not l1:
                curr.next = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)
        