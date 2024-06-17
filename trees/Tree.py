# A basic Tree node implementation - Binary Search Tree


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right


left_node = TreeNode(25)
right_node = TreeNode(75)
root = TreeNode(50, left_node, right_node)


# Search Implementation for Binary Search Tree using recursion
# Search in a balanced binary search tree is O(log N).
# When a tree is completely imbalanced search is O(N)


def search(searchValue, node):
    if node is None or node.value == searchValue:
        return node
    elif searchValue < node.value:
        return search(searchValue, node.leftChild)
    else:
        return search(searchValue, node.rightChild)


# Example Usage:

# print(search(25, root))


# Insert Implementation for Binary Search Tree using recursion
# Insert in a binary search tree is O(log N).


def insert(value, node):
    if value < node.value:
        # If the left child does not exist, we want to insert the value as the left child:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    elif value > node.value:
        # If the right child does not exist, we want to insert the value as the right child:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)


# Example Usage:
# for the side with 25
insert(16, root)
insert(30, root)

# for the right side with 75
insert(60, root)
insert(85, root)
