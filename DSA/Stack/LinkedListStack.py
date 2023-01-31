class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    #Constructor
    def __init__(self):
        self.head = None
     
    #Yield node data
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        stack = [str(x) for x in self.LinkedList]
        return '\n'.join(stack)
        
    def is_empty(self) :
        if not self.LinkedList.head:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty(): return "Stack is empty"
        return self.LinkedList.head.data
    
    def push(self, data):
        val = Node(data)
        if self.is_empty():
            self.LinkedList.head = val
        else:
            val.next = self.LinkedList.head
            self.LinkedList.head = val
        return

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        curr = self.LinkedList.head
        if not self.LinkedList.head.next:
            self.LinkedList.head = None
        else:
             self.LinkedList.head = self.LinkedList.head.next
        return f'{curr.data} popped off stack'



