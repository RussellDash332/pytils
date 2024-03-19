class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

# The not-so circular linked list
class LL:
    def __init__(self):
        self.tail = None
        self.size = 0
    def insert(self, node):
        if self.tail:
            if self.tail.next:
                self.tail.next.prev = node
                node.next = self.tail.next
            self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
    def insert_at(self, node, at):
        prev, curr, succ = at, node, at.next
        prev.next, curr.prev, curr.next, succ.prev = curr, prev, succ, curr
        if self.tail == prev:
            self.tail = curr
        self.size += 1
    def remove(self, node):
        if node.prev:   node.prev.next = node.next
        if node.next:   node.next.prev = node.prev
        if self.tail == node:   self.tail = node.prev
        node.next, node.prev = None, None
        self.size -= 1
        return node
    def print(self):
        arr = []
        curr = self.tail
        for _ in range(self.size):
            arr.append(curr.val)
            curr = curr.prev
        for i in range(self.size - 1, -1, -1):
            print(arr[i])