class Node:
    """
    Represents a node in a binary tree.

    Attributes:
    - value: The value stored in the node.
    - left: Reference to the left child node.
    - right: Reference to the right child node.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the Node class.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


def pre_order(root):
    """
    Perform pre-order traversal on a binary tree.

    Parameters:
    - root: The root node of the binary tree.

    Prints the values of nodes in the order: root, left subtree, right subtree.
    """
    if root:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    pre_order(root)
