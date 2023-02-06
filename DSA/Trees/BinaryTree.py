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
       /   \
      L1    R1
     /  \  /  \
    L2  R2 L3  R3

PreOrder Traversal: A, L1, L2, R2, R1, L3, R3
InOrder Traversal: L2, L1, R2, A, L3, R1, R3
PostOrder Traversal: L2, R2, L1, L3, R3, R1, A

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

from collections import deque
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(str(node.data))
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


levelOrder(custom)