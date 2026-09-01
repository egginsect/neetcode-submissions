"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    copied = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        if head in self.copied:
            return self.copied[head]
        newHead = Node(head.val)
        self.copied[head] = newHead
        newHead.next = self.copyRandomList(head.next)
        newHead.random = self.copyRandomList(head.random)
        return self.copied[head]
        