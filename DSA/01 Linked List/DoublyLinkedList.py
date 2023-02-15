class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.tail = None
    
    def __repr__(self):
        return self.data

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        vals = [str(val.data) for val in self]
        return '->'.join(vals)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def add(self, data):
        val = Node(data)
        if not self.head:
            self.head = val
            self.tail = val
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = val
            val.prev = curr
            self.tail = val

    def delete(self, index):
        if index == 1:
            self.head = self.head.next
            self.head.next.prev = None 
            return
        curr = self.head
        count = 2
        while count < index:
            curr = curr.next
            count += 1
        curr.next = curr.next.next
        curr.next.next.prev = curr
