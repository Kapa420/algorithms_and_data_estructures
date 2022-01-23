"""Implementation functions for the code."""

from Data.binarytree import AVL_Tree

menu_options = {
    1: "Add a node",
    2: "Remove a node",
    3: "Print",
    4: "Search a node",
    5: "Find the minimum value on the tree.""",
    6: "Find the maximum value on the tree.""",
    7: "End all"
}
options_print = {
    1: "postOrder",
    2: "inOrder",
    3: "preOrder"
}


def opt_findMax(tree):
    """Print option findMax."""
    print(tree.findMax(root))
    print("*-*-*-*-*-*-*-*-", "\n", "\n")


def opt_findMin(tree):
    """Print option findMin."""
    print(tree.findMin(root))
    print("*-*-*-*-*-*-*-*-", "\n", "\n")


def opt_find(tree):
    """Find option."""
    key = int(input("Insert the number to search: "))
    print(tree.find(key, root))
    print("*-*-*-*-*-*-*-*-", "\n", "\n")


def opt_print(tree):
    """Print option."""
    for op_print in options_print:
        print(str(op_print) + ":", options_print[op_print])
    opt = int(input())
    if opt == 1:
        tree.postOrder(root)
    elif opt == 2:
        tree.inOrder(root)
    elif opt == 3:
        tree.preOrder(root)
    else:
        pass
    print("\n", "\n", "*-*-*-*-*-*-*-*-", "\n", "\n")


def opt_remove(tree):
    """Remove option."""
    key = int(input("Insert a number: "))
    tree.delete(root, key)
    print(f'{key} removed from the tree')
    print("\n", "\n", "*-*-*-*-*-*-*-*-", "\n", "\n")


if __name__ == '__main__':
    tree = AVL_Tree()
    root = None
    while True:
        for option in menu_options:
            print(str(option) + ":", menu_options[option])
        option = int(input("Option: "))
        if option == 1:
            key = int(input("Insert a number: "))
            root = tree.insert(root, key)
            print(f'{key} added to the tree')
            print("\n", "\n", "*-*-*-*-*-*-*-*-", "\n", "\n")

        elif option == 2:
            opt_remove(tree)
        elif option == 3:
            opt_print(tree)
        elif option == 4:
            opt_find(tree)
        elif option == 5:
            opt_findMax(tree)
        elif option == 6:
            opt_findMin(tree)
        else:
            print("Thanks)")
            break
