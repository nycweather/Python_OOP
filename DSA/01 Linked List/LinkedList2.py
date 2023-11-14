class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None 

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.data})'
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self, node:Node)->None:
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next
    
    def __str__(self):
        if not self.head:
            return "This LinkedList is empty"
        else:
            vals = [str(x) for x in self]
            return "->".join(vals)

                
    
    
node1 = Node(14)
node2 = Node(15)
node3 = Node(16)
node4 = Node(17)
linkedlist = LinkedList()
linkedlist.add(node1)
linkedlist.add(node2)
linkedlist.add(node3)
linkedlist.add(node4)
print(linkedlist)
