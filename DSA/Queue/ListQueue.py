class Queue:
    def __init__(self):
        '''
        Constructor.
        This queue will be implemented through python list with unlimited array size.
        '''
        self.list = []

    def __str__(self):
        '''
        Returns current queue list.
        '''
        vals = [str(x) for x in self.list]
        return '->'.join(vals)

    def is_empty(self):
        if self.list == []: return True
        else: return False

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if self.is_empty(): return 'Queue is empty'
        else: self.list = self.list[1::]

    def peek(self):
        if self.is_empty(): return 'List is empty'
        else:
            return self.list[0]
    