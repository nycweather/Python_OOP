class Heap:
    def __init__(self, size):
        self.list = [None] * (size + 1)
        self.heapSize = 0
        self.maxSize = size + 1

def peek(root):
    if not root:
        return
    return root.list[1]

def size(root):
    if not root:
        return
    return f"Number of elements in heap: {root.heapSize}"

def levelOrder(root):
    if not root:
        return []
    else:
        result = []
        for i in range(1, root.heapSize+1):
            result.append(root.list[i])
        return result

def heapify(root, index, type):
    if index <= 1:
        return
    parentIndex = int(index/2)
    if type == 'Min':
        if root.list[index] < root.list[parentIndex]:
            temp = root.list[index]
            root.list[index] = root.list[parentIndex]
            root.list[parentIndex] = temp
        heapify(root, parentIndex, type)
    elif type == 'Max':
        if root.list[index] > root.list[parentIndex]:
            temp = root.list[index]
            root.list[index] = root.list[parentIndex]
            root.list[parentIndex] = temp
        heapify(root, parentIndex, type)

def insert(root, data, type):
    if root.heapSize + 1 == root.maxSize:
        return "Heap is full"
    root.list[root.heapSize+1] = data
    root.heapSize += 1
    heapify(root, root.heapSize, type)
    return "Inserted"



custom = Heap(5)
print(size(custom))
insert(custom, 5, "Max")
# insert(custom, 18, "Max")
insert(custom, 17, "Max")
insert(custom, 4, "Max")
insert(custom, 18, "Max")
# insert(custom, 4, "Max")
print(levelOrder(custom))
print(size(custom))

