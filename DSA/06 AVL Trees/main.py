class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

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

def insert(root, val):
    # Normal BST insert
    if not root.data:
        root.data = val
    elif root.data >= val:
        if root.left is None:
            root.left = Node(val)
        else:
            insert(root.left, val)
    else:
        if root.right is None:
            root.right = Node(val)
        else:
            insert(root.right, val)
    
    # Update height of original node
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # Check if rotation needs to be performed 
    balance = getBalance(root)

    # 4 different cases for balancing the tree
    # Left Left Case
    if balance > 1 and val < root.left.data:
        return rightRotate(root)
    
    # Right Right Case
    if balance < -1 and val > root.right.data:
        return leftRotate(root)

    # Left Right Case
    if balance > 1 and val > root.left.data:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Right Left Case
    if balance < -1 and val < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def getHeight(root):
    if not root:
        return 0
    return root.height

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def leftRotate(root):
    newRoot = root.right
    newRight = newRoot.right

    # Rotate
    newRoot.left = root
    root.right = newRight

    # Update heights
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))

    # Return the new root
    return newRoot

def rightRotate(root):
    newRoot = root.left
    newLeft = newRoot.right

    # Rotate
    newRoot.right = root
    root.left = newLeft

    # Update heights
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))

    # Return the new root
    return newRoot


custom = Node(50)
insert(custom, 10)
insert(custom, 20)
insert(custom, 30)
insert(custom, 40)
insert(custom, 50)
insert(custom, 60)
insert(custom, 70)
insert(custom, 80)


print(levelOrder(custom))

