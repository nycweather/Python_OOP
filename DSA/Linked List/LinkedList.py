##LinkedList

class Node:

    #Constructor
    def __init__(self, data):
        self.next = None 
        self.data = data 
    
    #Get string values
    def __repr__(self):
        return self.data
    

class SinglyLinkedList:
    #Constructor
    def __init__(self, head=None) -> None:
        self.head = head

    #'Show' the structure of the list
    def __str__(self):
        vals = [str(val.data) for val in self]
        return "->".join(vals)

    #Give the ability to loop over the list
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    #Add data to list, if list does not have a head current node will become the head
    def add(self, data):
        val = Node(data)
        if not self.head:
            self.head = val
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = val
        return f'Added {data} to list'

    #Return how many elements are in the list
    def count(self):
        if not self.head:
            return 0
        else:
            count = 0
            curr = self.head
            while curr:
                count += 1
                curr = curr.next
            return count

    def add_to_first(self, data):
        val = Node(data)
        val.next = self.head
        self.head = val

    #insert node at give index
    def add_at_index(self, index: int, data):
        assert index >= 1, f"Index {index} not greater than 1."
        if index == 1:
            return self.add_to_first(data)
        else:
            if index > self.count():
                self.add(data)
                print(f"{data} added at the end of the list")
            else:
                curr = self.head
                count = 2
                while count < index:
                    curr = curr.next
                    count += 1
                temp = curr.next
                curr.next = Node(data)
                curr.next.next = temp

    #delete node given index            
    def delete(self, index):
        assert index >= 1, f"Index {index} is less than 1."
        if not self.head:
            return "List is empty"
        else:
            if index > self.count():
                return "Out of bounds"
            else:
                if index == 1:
                    self.head = self.head.next
                    return 0
                curr = self.head
                count = 2
                while count<index:
                    count += 1
                    curr = curr.next
                try:
                    curr.next = curr.next.next
                except:
                    curr.next = None

    #search given item
    def search(self, val):
        if not self.head:
            return 0
        else:
            curr = self.head
            count = 1
            while not curr or curr.data !=  val:
                curr = curr.next
                count += 1
            if curr.data == val:
                return f"{val} at index {count}"
            return "{val} not in list"

    #pop mrthod to pop off last element
    def pop(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        print(f'{curr.next.data} popped')
        curr.next = None
        return

    #reverse list 
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return 0

        


            

