# Program to insert a node in AVL tree and balancing it.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):
    '''insert key in subtree rooted with node and return new root of subtree'''

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # if node is unbalanced check 4 cases
        # case 1 - left left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # case 2 - right right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # case 3 - left right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # case 4 - right left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.val:
            self.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.right
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        # if tree has only one node , simply return it
        if root is None:
            return root

        # update the height of ancester node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # left left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.leftRotate(root)

        # right right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rightRotate(root)

        # left right
        if balance > 1 and self.getBalance(root.left) < 0:
            self.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right left
        if balance < -1 and self.getBalance(root.right) > 0:
            self.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):  # z is root of subtree
        y = z.right
        T2 = y.left

        # rotation performed
        y.left = z
        z.right = T2

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # rotation performed
        y.right = z
        z.left = T3

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):

        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return

        print(f'{root.val}', end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

# now test it


newTree = AVL_Tree()
root = None
root = newTree.insert(root, 20)

arr = [34, -22, 56, -1, 90, 0]

for a in arr:
    root = newTree.insert(root, a)

print('preOrder traversal of AVL tree is')
newTree.preOrder(root)

key = 0

root = newTree.delete(root, key)

print(f'\nOutput after deletion is of {key}')
newTree.preOrder(root)
