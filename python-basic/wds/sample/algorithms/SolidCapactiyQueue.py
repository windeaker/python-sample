class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def next(self):
        return self.next

    def value(self):
        return self.value


class SolidCapacityQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def offer(self, value):
        node = Node(value, None)
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size = self.size + 1
        if self.size > self.capacity:
            self.poll()

    def poll(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            node.next = None
            self.size = self.size - 1
