##LinkedList

class Node:
    def __init__(self, data):
        '''
        Constructor.
        Data will contain the data inside each node.
        Next will refer to the next node.
        '''
        self.data = data 
        self.next = None 
    
    def __repr__(self):
        '''
        This method will return the string method of Node data.
        '''
        return self.data
    

class SinglyLinkedList:
    """
    This class will create a singly linked list.
    """
    def __init__(self, head=None):
        '''
        When first initialized this will be the start of the list.
        '''
        self.head = head

    def __str__(self):
        '''
        This method will iter through the whole list and return it.
        '''
        vals = [str(val.data) for val in self]
        return "->".join(vals)

    def __iter__(self):
        '''
        This will give the ability to loop over.
        '''
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    #Add data to list, if list does not have a head current node will become the head
    def add(self, data):
        '''
        This method will take in a data, create the node and chain to the end of the list.
        '''
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
        '''
        This item will iter thorugh the list and count how many items are in the list.
        '''
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
        '''
        This item will take in data, create a Node and put it in at the beginning of the list.
        '''
        val = Node(data)
        val.next = self.head
        self.head = val

    #insert node at give index
    def add_at_index(self, index: int, data):
        '''
        This method will take in two arguments (index) and data, create the Node and insert it within the list.
        '''
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
        '''
        Delete a node given the index number.
        '''
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
        '''
        Search through the list and returns string if item in list.
        '''
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

    #pop method to pop off last element
    def pop(self):
        '''
        Deletes last item off list.
        '''
        curr = self.head
        while curr.next.next:
            curr = curr.next
        print(f'{curr.next.data} popped')
        curr.next = None
        return

    #reverse list 
    def reverse(self):
        '''
        Reverse the list.
        '''
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return 0

        


            

