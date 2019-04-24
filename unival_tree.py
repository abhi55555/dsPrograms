# program to find number of universal value trees in a given tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countTree(root, count):
    if root is None:
        return True

    left = countTree(root.left, count)
    right = countTree(root.right, count)

    if left == False or right == False:
        return False

    if root.left and root.data != root.left.data:
        return False
    if root.right and root.data != root.right.data:
        return False

    count[0] += 1
    return True


def countMain(root):
    count = [0]

    countTree(root, count)
    return count[0]


root = Node(9)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(4)
countMain(root)
print("Count of Single Valued Subtress is", countMain(root))
