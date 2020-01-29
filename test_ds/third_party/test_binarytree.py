from binarytree import tree, bst, heap
from binarytree import Node

def test_tree_types():
    # Generate a random binary tree and return its root node
    my_tree = tree(height=3, is_perfect=False)
    # Generate a random BST and return its root node
    my_bst = bst(height=3, is_perfect=True)
    # Generate a random max heap and return its root node
    my_heap = heap(height=3, is_max=True, is_perfect=False)
    # Pretty-print the trees in stdout
    print("binary tree")
    print(my_tree)
    print("bst")
    print(my_bst)
    print("heap")
    print(my_heap)

def test_sample_tree_1():
    root = Node(5)
    root.left = Node(1)
    root.right = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(9)
    root.right.left.left = Node(4)
    root.right.left.right = Node(7)
    print(root)

