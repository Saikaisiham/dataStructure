class Node: 
    """
    Represents a node in a binary tree.

    Attributes: 
    -value: The value stored in the code 
    -left: References to the left child node 
    -right: References to the right child in the node
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


def print_inorder(root): 
    """
    Perform pre-order traversal on a binary tree.

    Parameters:
    - root: The root node of the binary tree.

    Prints the values of nodes in the order: left subtree, root, right subtree.
    """
    if root: 
        print_inorder(root.left)
        print(root.value, end=' ')
        print_inorder(root.right)




if __name__ == '__main__': 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
 
    print_inorder(root)



