# Write an algorithm that finds the greatest value within a binary search tree.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right


left_node = TreeNode(25)
right_node = TreeNode(75)
root = TreeNode(50, left_node, right_node)


def greatest_value(node):
    if node.rightChild:
        return greatest_value(node.rightChild)
    else:
        return node.value


# Exampple Usage:
value = greatest_value(root)
print(value)  # 75
