class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k

def treeSize(root):
    if root is None:
        return 0
    else:
        ls = treeSize(root.left)
        rs = treeSize(root.right)
        return ls + rs + 1
    
# Create the binary tree
root = Node(10)
root.left = Node(20)
root.left.right = Node(50)
root.left.left = Node(40)
root.right = Node(30)

# Calculate the size of the tree
size = treeSize(root)
print("Size of the tree:", size)
