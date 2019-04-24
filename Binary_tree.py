class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        def __str__(self):
            return str(self.info)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        current = self.root

        while(True):
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            elif val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break

            else:
                break


tree = BinaryTree()

arr = [6, 1, 0, -7, 7, 8, 78]

for a in arr:
    tree.insert(a)

inorder(tree.root)
