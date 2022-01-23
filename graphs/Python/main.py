"""."""
from Data.binarytree import AVL_Tree

myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2, 50]

for num in nums:
    root = myTree.insert(root, num)
    print(root.val)


# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()

# insert
root = myTree.insert(root, 20)

root = myTree.insert(root, 150)

# Delete
root = myTree.delete(root, 10)

# Preorder Traversal
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
print('\n')
myTree.postOrder(root)
print('\n')
myTree.inOrder(root)
print()
print(myTree.findMax(root))
print(myTree.find(50, root))
