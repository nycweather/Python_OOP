class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return '->'.join(values)
    
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.is_full():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first = self.items[self.start]
            start = self.start
            #Queue is empty 
            if self.start == self.top:
                self.start = -1
                self.top = -1
            #restart queue
            elif self.start + 1 == self.maxSize:
                self.start = 0
            #Point to next index
            else:
                self.start += 1
            self.items[start] = None
            return first

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.lists = [None] * self.maxSize
        self.top = -1
        self.start = -1