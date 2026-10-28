class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.ref = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_tail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.ref:
            node = self.ref[key]
            self.remove(node)
            self.insert_at_tail(node)
            return node.val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.ref:
            node = self.ref[key]
            node.val = value
            self.remove(node)
        else:
            if len(self.ref)>=self.capacity:
                self.ref.pop(self.head.next.key)
                self.remove(self.head.next)
            node = Node(key, value)
        self.insert_at_tail(node)
        self.ref[key] = node

        
