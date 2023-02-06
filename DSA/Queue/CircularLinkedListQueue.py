class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def __str__(self):
        vals = [str(x.data) for x in self.list]
        return '->'.join(vals)

    def is_empty(self):
        if self.list.head: return False
        else: return True

    def enqueue(self, data):
        if self.is_empty():
            self.list.head = Node(data)
        else:
            curr = self.list.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def dequeue(self):
        if self.is_empty():
            return "List is empty"
        else:
            try:
                self.list.head = self.list.head.next
            except:
                self.list.head = None

    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        else:
            return self.list.head.data
