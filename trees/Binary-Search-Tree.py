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


def delete(valueToDelete, node):

    # The base case is when we've hit the bottom of the tree,
    # and the parent node has no children:
    if node is None:
        return None
    # If the value we're deleting is less or greater than the current node,
    # we set the left or right child respectively to be
    # the return value of a recursive call of this
    # very method on the current
    # node's left or right subtree.
    elif valueToDelete < node.value:
        node.leftChild = delete(valueToDelete, node.leftChild)
    # We return the current node (and its subtree if existent) to
    # be used as the new value of its parent's left or right child:
        return node
    elif valueToDelete > node.value:
        node.rightChild = delete(valueToDelete, node.rightChild)
        return node
    # If the current node is the one we want to delete:
    elif valueToDelete == node.value:
        # If the current node has no left child, we delete it by
        # returning its right child (and its subtree if existent)
        # to be its parent's new subtree:
        if node.leftChild is None:
            return node.rightChild
    # (If the current node has no left OR right child, this ends up
    # being None as per the first line of code in this function.)
    elif node.rightChild is None:
        return node.leftChild
    # If the current node has two children, we delete the current node
    # by calling the lift function (below),
    # which changes the current node's
    # value to the value of its successor node:
    else:
        node.rightChild = lift(node.rightChild, node)
        return node


def lift(node, nodeToDelete):

    # If the current node of this function has a left child,
    # we recursively call this function to continue down
    # the left subtree to find the successor node.
    if node.leftChild:
        node.leftChild = lift(node.leftChild, nodeToDelete)
        return node

    # If the current node has no left child, that means the current node
    # of this function is the successor node, and we take its value
    # and make it the new value of the node that we're deleting:
    else:
        nodeToDelete.value = node.value
        # We return the successor node's right child to be now used
        # as its parent's left child:
        return node.rightChild


print(pow(2, 10))
