
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create Tree: RENZ LAREÑO
root = Node("R")

root.left = Node("E")
root.right = Node("N")

root.left.left = Node("Z")
root.left.right = Node("L")

root.right.left = Node("A")
root.right.right = Node("R")

root.left.left.left = Node("E")
root.left.left.right = Node("Ñ")

root.left.right.left = Node("O")


print("Preorder (Root, Left, Right):")
preorder(root)

print("\n\nInorder (Left, Root, Right):")
inorder(root)

print("\n\nPostorder (Left, Right, Root):")
postorder(root)
