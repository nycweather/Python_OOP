class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        self.list.reverse()
        vals = [str(val) for val in self.list]
        return '\n'.join(vals)

    def is_empty(self):
        if self.list==[]: return True
        else: return False

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty(): return 'Stack is empty'
        else: return self.list.pop()

    def peek(self):
        if self.is_empty(): return 'Stack is empty'
        else: return self.list[-1]

    def delete(self):
        if self.is_empty(): return 'Stack is empty'
        else: self.list = []