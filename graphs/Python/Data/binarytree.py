"""Implementation of a AVL binary search tree."""
from Data.nodes import TreeNode


class AVL_Tree(object):
    """Class for the AVL binary tree."""

    def __init__(self):
        """Set constructor for AVL_tree."""
        self.root = None

    def insert(self, root, key):
        """Insert a node in the tree."""
        if root is None:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def delete(self, root, key):
        """Delete a node from the tree."""
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.findMin(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        """Set a simple left rotation."""
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        """Set a simple right rotation."""
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        """Get the height of the tree."""
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        """Get balance of the tree."""
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def findMin(self, root):
        """Recursivly get the minimum value of the tree."""
        if root is None or root.left is None:
            return root.val
        return self.findMin(root.left)

    def findMax(self, root):
        """Recursivly get the maximum value of the tree."""
        if root is None or root.right is None:
            return root.val
        return self.findMax(root.right)

    def preOrder(self, root):
        """Return the tree in the preorder form."""
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        """Return the tree in the postorder form."""
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print("{0} ".format(root.val), end="")

    def inOrder(self, root):
        """Return the tree in the postorder form."""
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.val), end="")
        self.inOrder(root.right)

    def find(self, key, node):
        """Find if a value is on the tree."""
        if not node:
            return False
        elif key < node.val:
            return self.find(key, node.left)
        elif key > node.val:
            return self.find(key, node.right)
        else:
            return True
