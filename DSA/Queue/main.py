from CircularLinkedListQueue import Queue

custom = Queue()

print(custom)
print(custom.is_empty())
custom.enqueue(1)
custom.enqueue(2)
custom.enqueue(3)
print(custom)
print(custom.peek())
custom.enqueue(4)
custom.enqueue(5)
# custom.enqueue(6)
# print(custom)
custom.dequeue()
print(custom)
# print(custom.peek())