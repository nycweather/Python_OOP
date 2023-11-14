class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return self.val

    def __del__(self):
        # print(f"{self.val} deleted", end=", ")
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        arr = [str(x.val) for x in self]
        return "->".join(arr)
    
    def __iter__(self):
        if not self.head:
            return None
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
        return

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            self.length+=1
            return
        curr = self.head 
        while (curr.next):
            curr = curr.next
        curr.next = node
        node.prev = curr
        self.tail = node
        self.length += 1
        return
    
    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            temp = self.head
            self.head = None
            self.tail = None
            return temp.val
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return temp.val
    
    def shift(self):
        if not self.head:
            return None 
        if not self.head.next:
            return self.head.val
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp.val
    
    def unshift(self, val):
        if not self.head:
            self.push(val)
            return
        node = Node(val)
        temp = self.head
        self.head = node
        node.next = temp
        temp.prev = node
        return


    
my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)
my_list.unshift(5)
print(my_list)