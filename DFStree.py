
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create Tree
root = Node("R")
root.left = Node("E")
root.right = Node("N")
root.right.right = Node("Z")


print("DFS Preorder:")
preorder(root)

print("\nDFS Inorder:")
inorder(root)

print("\nDFS Postorder:")
postorder(root)
