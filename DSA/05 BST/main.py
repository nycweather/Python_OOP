class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, val):
    if not root.data:
        root.data = val
    elif root.data >= val:
        if root.left is None:
            root.left = BST(val)
        else:
            insert(root.left, val)
    else:
        if root.right is None:
            root.right = BST(val)
        else:
            insert(root.right, val)

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def levelOrder(root):
    result = []
    if not root:
        return result
    queue = [root]
    count = 0
    while queue:
        level = []
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        count+=1
        result.append(level)
    print("Total levels: " + str(count))
    return result

def search(root, val):
    if not root:
        return False
    if root.data == val:
        return True
    elif root.data > val:
        return search(root.left, val)
    else:
        return search(root.right, val)

def getMin(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr.data

def delete(root, val):
    if not root:
        return 
    if root.data > val:
        root.left = delete(root.left, val)
    elif root.data < val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min = getMin(root.right)
            root.data = min
            root.right = delete(root.right, min)
    return

custom = BST(None)
insert(custom, 70)
insert(custom, 50)
insert(custom, 90)
insert(custom, 30)
insert(custom, 60)
insert(custom, 80)
insert(custom, 100)
insert(custom, 20)
insert(custom, 40)

#print(custom.data)
print(levelOrder(custom))
print(search(custom, 45))
print(getMin(custom))
delete(custom, 80)
print(levelOrder(custom))