class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if not current:
                return -1
            current = current.next
        if current is None: 
            return -1
        else:
            return current.val

    def insertHead(self, val: int) -> None:
        body = self.head
        self.head = Node(val)
        self.head.next = body

    def insertTail(self, val: int) -> None:
        prev, current = None, self.head
        while current:
            prev, current = current, current.next
        if prev: 
            prev.next = Node(val)
        else: 
            self.insertHead(val)
        

    def remove(self, index: int) -> bool:
        """
        -1 -> 0 -> 1
        0
        -1 -> 0 

        """
        dummy = Node(-1)
        dummy.next = self.head
        current = dummy
        for _ in range(index):
            if not current.next:
                return False
            current = current.next
        if not current.next:
            return False
        current.next = current.next.next
        self.head = dummy.next
        return True

    def getValues(self) -> List[int]:
        current = self.head
        out = []
        while current:
            out.append(current.val)
            current = current.next
        return out
