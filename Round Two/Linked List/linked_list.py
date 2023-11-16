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
    """Linked List Class"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        arr = [str(node.val) for node in self]
        return "->".join(arr)
    
    def __iter__(self):
        if not self.head:
            return None
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
        return
    
    def __len__(self):
        return self.length
    
    def __contains__(self, val):
        curr = self.head
        while curr is not None:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def __del__(self):
        print(f"{self.__class__.__name__} object deleted from {self.__class__}")

    def __sizeof__(self) -> int:
        return self.length

    def push(self, val, index=None):
        if index is None or index >= self.length:
            self._push_to_end(val)
        else:
            self._push_using_index(val, index)

    def _push_using_index(self, val, index):
        if index >= self.length:
            self._push_to_end(val)
        if index == 0:
            self.unshift(val)
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            node.prev = curr
            curr.next = node
            self.length += 1
            return
        
    def _push_to_end(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            return
        curr = self.head 
        while (curr.next):
            curr = curr.next
        curr.next = node
        node.prev = curr
        self.tail = node
        self.length += 1
        return
    
    def pop(self, index = None):
        if index is None or index >= self.length:
            self._delete_last_node()
        elif index == 0:
            self.shift()
        else:
            self._delete_node(index)
    
    def _delete_last_node(self):
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
        self.length -= 1
        return temp.val
    
    def _delete_node(self, index):
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        if curr.next.next:
            curr.next = curr.next.next
            curr.next.prev = curr
        else:
            curr.next = None
        self.length -= 1
        return
        
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
    
    def reverse(self):
        if not self.head or not self.head.next:
            return 
        curr = self.head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def cycle(self):
        slow, fast = self.head, self.head.next
        while slow:
            if slow == fast:
                return True
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
        return False
    

    
my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)
my_list.push(5)
print(my_list)
my_list.reverse()
# my_list.pop(9)
# my_list.unshift(5)
# my_list.shift()
print(my_list)

temp = LinkedList.__dict__
