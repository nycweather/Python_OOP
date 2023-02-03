class Queue:
    def __init__(self, maxSize):
        self.list = [None] * maxSize
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        vals = [str(val) for val in self.list]
        return '\n'.join(vals)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif (self.start == 0) and (self.top + 1 == self.maxSize): 
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else: 
            return False

    def enqueue(self, data):
        if self.is_full:
            print("Queue is full")
            return
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = data
            print(f'{data} added')
            return "Element inserted at the end of the queue"
