class BinaryTree:
    '''
    Each node should contain a data and the two pointers left and right.
    First node will be root node after that everything else will be its children.
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Adding Nodes
custom = BinaryTree('A')
L1 = BinaryTree('L1')
R1 = BinaryTree('R1')
L2 = BinaryTree('L2')
R2 = BinaryTree('R2')
L3 = BinaryTree('L3')
R3 = BinaryTree('R3')
#Linking Nodes
custom.left = L1
custom.right = R1
L1.left = L2
L1.right = R2
R1.left = L3
R1.right = R3



'''
Intended tree
             A
        /         \
      L1            R1
    /    \       /    \
   L2     R2    L3     R3
  / \    / \   / \     / \
L4  R4  L5 R5 L6 R6   L7  R7

PreOrder Traversal: A, L1, L2, R2, R1, L3, R3
InOrder Traversal: L2, L1, R2, A, L3, R1, R3
PostOrder Traversal: L2, R2, L1, L3, R3, R1, A
LevelOrder Traversal: A, L1, R1, L2, R2, L3, R3
'''
    
def preOrder(rootNode):
    '''
    This fuction will print root node and continue on the left side of the tree as song as it has a child.
    If left child does not exist it will pop up the stack and goto the right child.
    And if the right child has a left node it will go down that left node.
    '''
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)


def inOrder(rootNode):
    '''
    This function will goto the deepest left node then print node then goto right and goto the deepest left node of the right child and continue.
    '''
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)


def postOrder(rootNode):
    '''
    Visit all the children before their parent node.
    '''
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)


def levelOrder(root):
    '''
    Print in order of level by level.
    Using a queue it will append each level.
    And using a for loop it will check how many nodes to add to each level.
    '''
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

def levelOrderOneList(root):
    '''
    Similar to level order traversal but it will return one list instead of nested list
    '''
    if not root:
        return False 
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

        

def searchBinaryTree(root, val):
    '''
    Search the binary tree in similar fashion to level order traversal
    '''
    if not root:
        return False
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.data == val:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

def insertInto(root, data):
    if not root:
        return BinaryTree(data)
    queue = [root]
    #loop through whole tree
    while queue:
        node = queue.pop(0)
        #If not does not exist on the left it will insert to left
        if not node.left:
            node.left = BinaryTree(data)
            return
        #If not does not exist on the right it will insert to right
        if not node.right:
            node.right = BinaryTree(data)
            return
        #Else if nodes exist add to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def deepestNode(root):
    if not root:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return node

def deleteDeepestNode(root):
    if not root:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    node = None

def deleteNode(root, data):
    if not root:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.data == data:
            node.data = deepestNode(root).data
            return
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return
        

insertInto(custom, "L4")
insertInto(custom, "R4")
insertInto(custom, "L5")
insertInto(custom, "R5")
insertInto(custom, "L6")
insertInto(custom, "R6")
insertInto(custom, "L7")
insertInto(custom, "R7")

###########################
print(deepestNode(custom).data)
print("____")
deleteNode(custom, "R6")

print(levelOrder(custom))

print(deepestNode(custom).data)