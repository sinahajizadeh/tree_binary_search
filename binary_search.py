class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

def findLargestElement(root):
    if root==None:
        return False
    elif root.rightChild==None:
        return root.data
    else:
        return findLargestElement(root.rightChild)

def search(root,value):
    if root==None:
        return False
    elif root.data==value:
        return True
    elif root.data <value:
        return search(root.rightChild,value)
    else:
        return search(root.leftChild,value)